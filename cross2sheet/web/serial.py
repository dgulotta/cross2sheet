import json

from cross2sheet.grid_features import BackgroundElt,TextElt,BorderElt

class TableData:
    def __init__(self,width=None,height=None,back=None,bars=None,text=None,*,img=None):
        if img:
            g=img.grid()
            self.width=g.width
            self.height=g.height
            self.back=img.read_background()
            self.bars=img.read_bars()
            self.text=img.autonumber_if_text_found()
        else:
            self.width=width
            self.height=height
            self.back=back
            self.bars=bars
            self.text=text

    def to_json(self):
        d={
            'width' : self.width,
            'height' : self.height,
            'back' : [(r,c,e.color) for r,c,e in self.back],
            'bars' : [(r,c,e.dirs) for r,c,e in self.bars],
            'text' : [(r,c,e.text) for r,c,e in self.text]
        }
        return json.dumps(d)

    @staticmethod
    def from_json(s):
        d=json.loads(s)
        return TableData(width=d['width'],height=d['height'],
            back=[(r,c,BackgroundElt(b)) for r,c,b in d['back']],
            bars=[(r,c,BorderElt(b)) for r,c,b in d['bars']],
            text=[(r,c,TextElt(t)) for r,c,t in d['text']])
