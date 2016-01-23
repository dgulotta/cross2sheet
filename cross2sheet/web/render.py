from bs4 import Tag
from cross2sheet.grid_features import Grid
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
    def __init__(self,data):
        self.cells = [[Cell() for x in range(data.width)] for y in range(data.height)]
        for r,c,e in data.back:
            self.cells[r][c].back=e.color
        for r,c,e in data.bars:
            self.cells[r][c].borders.extend(b.lower() for b in e.dirs)
        for r,c,e in data.text:
            self.cells[r][c].texts.append(CellText(['text'],e.text))
        g=Grid(data.height,data.width)
        for s1,e1 in [('bar',data.bars),('nobar',[])]:
            for s2,e2 in [('back',data.back),('noback',[])]:
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
