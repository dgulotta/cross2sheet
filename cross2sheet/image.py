import itertools, statistics
import cv2, numpy
import tempfile, os, subprocess
from cross2sheet.grid_features import *

class ImageGrid:

    def __init__(self,data):
        if not data:
            raise ValueError('Image is empty')
        self.img=self.read_img(data)
        self.gray=cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        self.breaks=self.detect_breaks()

    @staticmethod
    def read_img(data):
        img=ImageGrid.decode_img(data)
        if img is not None:
            return img
        from wand.image import Image
        img=ImageGrid.decode_img(Image(blob=data,resolution=200).make_blob('png'))
        if img is not None:
            return img
        raise ValueError('Image data not recognized')


    @staticmethod
    def decode_img(data):
        arr=numpy.asarray(bytearray(data),dtype=numpy.uint8)
        return cv2.imdecode(arr,cv2.IMREAD_COLOR)

    def detect_breaks(self):
        _,thr = cv2.threshold(self.gray,214,255,cv2.THRESH_BINARY)
        _,con,_ = cv2.findContours(thr,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        squares=[c for c in con if self._contour_is_square(c) and cv2.contourArea(c)>=16]
        if not squares:
            return ([],[])
        a=statistics.median(cv2.contourArea(c) for c in squares)
        p=statistics.median(cv2.arcLength(c,True) for c in squares)
        blanks=[c for c in con if abs(cv2.contourArea(c)-a)<.1*a and abs(cv2.arcLength(c,True)-p)<.05*p]
        dist=int(p/8)
        yc = sorted({c[0,1] for s in blanks for c in s})
        xc = sorted({c[0,0] for s in blanks for c in s})
        return (self._squares_to_breaks(yc,dist),self._squares_to_breaks(xc,dist))

    def grid(self):
        return Grid(*self.dimensions())

    def dimensions(self):
        return (len(self.breaks[0])-1,len(self.breaks[1])-1)

    def read_background(self,color_resolution=2):
        cells = []
        for r,ys in enumerate(self._cell_slices(0)):
            for c,xs in enumerate(self._cell_slices(1)):
                means = self.img[ys,xs].mean(axis=(0,1))
                vals = [255*int(round(x*color_resolution/255.))//color_resolution for x in means]
                rgb = vals[0]|(vals[1]<<8)|(vals[2]<<16)
                cells.append((r,c,BackgroundElt(rgb)))
        return cells

    @staticmethod
    def _contour_is_square(c):
        if len(c)!=4:
            return False
        _,_,w,h = cv2.boundingRect(c)
        return 3*w>=2*h and 3*h>=2*w

    @staticmethod
    def _squares_to_breaks(coords,dist):
        start=None
        end=None
        breaks=[]
        for c in coords:
            if start is None:
                start=c
                end=c
            elif c-end>=dist:
                breaks.append((start,end))
                start=c
                end=c
            else:
                end=c
        breaks.append((start,end))
        return breaks

    def _cell_slices(self,idx):
        it1 = iter(self.breaks[idx])
        it2 = iter(self.breaks[idx])
        next(it2,None)
        for (_,a),(b,_) in zip(it1,it2):
            yield slice(a+1,b)

    # This isn't too reliable yet.  Use transforms.autonumber if possible.
    def autonumber_if_text_found(self):
        n=itertools.count(1)
        numbers=[]
        for r,ys in enumerate(self._cell_slices(0)):
            for c,xs in enumerate(self._cell_slices(1)):
                if self._has_text_rect(self.gray[ys,xs]):
                    numbers.append((r,c,TextElt(str(next(n)))))
        return numbers

    @staticmethod
    def _find_text_rect(img):
        _,thr = cv2.threshold(img,128,1,cv2.THRESH_BINARY)
        _,con,_ = cv2.findContours(thr,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        if len(con)<=1:
            return None
        x,y,w,h=cv2.boundingRect(numpy.concatenate(con[:-1]))
        if w*h>=15:
            return (slice(y-1,y+h+1),slice(x-1,x+w+1))

    @staticmethod
    def _has_text_rect(img):
        _,thr = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
        _,con,_ = cv2.findContours(thr,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        if len(con)>=2:
            return True
        elif len(con)==1:
            x,y,w,h=cv2.boundingRect(numpy.concatenate(con[0]))
            return cv2.arcLength(con[0],True)>2*w+2*h
        else:
            return False

    def read_bars(self):
        hbars=self._find_bars(lambda x,y: (x,y))
        vbars=self._find_bars(lambda x,y: (y,x))
        bars=[(y,x,BorderElt('T')) for y,x in hbars]
        bars.extend((y,x,BorderElt('L')) for y,x in vbars)
        return bars

    def _find_bars(self,coord):
        b0,b1=coord(0,1)
        if len(self.breaks[b0])<=2:
            return []
        span = max(b-a for a,b in self.breaks[b0])
        means = []
        for a,(c1,c2) in enumerate(self.breaks[b0][1:-1]):
            dy=(span-c2+c1)//2
            c2+=dy
            c1=c2-span
            for b,s in enumerate(self._cell_slices(b1)):
                means.append((a+1,b,self.gray[coord(slice(c1,c2+1),s)].mean()))
        smeans=sorted(m[2] for m in means)
        thr=smeans[max(range(len(smeans)-1),key=lambda j: smeans[j+1]-smeans[j])]
        return [coord(a,b) for a,b,m in means if m<=thr]

    # This isn't too reliable yet.  Use transforms.autonumber if possible.
    def read_text_ocr(self,ocr_cmd='tesseract',allowed_chars='0123456789'):
        f,fn = tempfile.mkstemp(suffix='.png')
        os.close(f)
        elts=[]
        for r,ys in enumerate(self._cell_slices(0)):
            for c,xs in enumerate(self._cell_slices(1)):
                small = self.gray[ys,xs]
                rect = self._find_text_rect(small)
                if not rect:
                    continue
                small = small[rect]
                cv2.imwrite(fn,small)
                txt=subprocess.check_output([ocr_cmd,fn,'stdout','-psm','8','-c','tessedit_char_whitelist=%s'%allowed_chars],stderr=subprocess.DEVNULL).decode().strip()
                if txt:
                    elts.append((r,c,TextElt(txt)))
        os.remove(fn)
        return elts
