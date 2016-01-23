from bs4 import Tag
from cross2sheet.transforms import autonumber

class Cell:
    def __init__(self):
        self.back=None
        self.borders=[]
        self.texts=[]

    def tag(self):
        t=Tag(name='td')
        if self.borders:
            t['class']=self.borders
        if self.back is not None:
            t['style']='background-color: #%06x;'%self.back
        for x in self.texts:
            t.append(x.text_tag())
        for x in self.texts:
            t.append(x.div_tag())
        return t

class CellText:
    def __init__(self,cls,text):
        self.cls=cls
        self.text=text

    def text_tag(self):
        t=Tag(name='span')
        t['class']=self.cls+['n']
        t.string=self.text
        return t

    def div_tag(self):
        t=Tag(name='div')
        t['class']=self.cls+['comment']
        t['title']=self.text
        return t

class Table:
    def __init__(self,img):
        g=img.grid()
        self.cells = [[Cell() for x in range(g.width)] for y in range(g.height)]
        back=img.read_background()
        bars=img.read_bars()
        for r,c,e in back:
            self.cells[r][c].back=e.color
        for r,c,e in bars:
            self.cells[r][c].borders.extend(b.lower() for b in e.dirs)
        for r,c,e in img.autonumber_if_text_found():
            self.cells[r][c].texts.append(CellText(['text'],e.text))
        for s1,e1 in [('bar',bars),('nobar',[])]:
            for s2,e2 in [('back',back),('noback',[])]:
                g.features=e1+e2
                for r,c,e in autonumber(g):
                    self.cells[r][c].texts.append(CellText(['auto',s1,s2],e.text))

    def tag(self):
        tt=Tag(name='table')
        for r in self.cells:
            rt=Tag(name='tr')
            for c in r:
                rt.append(c.tag())
            tt.append(rt)
        return tt

    def __html__(self):
        return str(self.tag())
