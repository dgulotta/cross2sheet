"""
Reads grids that are formatted in HTML in the same way as those from the 2014-2015 MIT
Mystery Hunts (eg http://web.mit.edu/puzzle/www/2014/puzzle/sledgehammered/).
"""

import bisect, html.parser, re
from cross2sheet.grid_features import *

class _GridHTMLParser(html.parser.HTMLParser):
    
    row_re = re.compile(r'top:(\d+)px;')
    column_re = re.compile(r'left:(\d+)px;')
    color_re = re.compile(r'border-top:#([0-9A-Fa-f]+)')

    def __init__(self):
        super().__init__()
        self.elts = []
        self.active_elt = None

    def grid(self):
        cell_starts = [(y,x) for y,x,c in self.elts if isinstance(c,BackgroundElt)]
        xs = sorted({x for y,x in cell_starts})
        ys = sorted({y for y,x in cell_starts})
        g=Grid(len(ys),len(xs))
        g.features=[(bisect.bisect_right(xs,x)-1,bisect.bisect_right(ys,y)-1,c) for y,x,c in self.elts]
        return g

    def handle_starttag(self,tag,attrs):
        if tag!='div':
            return
        attrd = dict(attrs)
        try:
            style = attrd.get('style')
            y = int(self.column_re.search(style).groups()[0])
            x = int(self.row_re.search(style).groups()[0])
        except(AttributeError,TypeError):
            return
        cls = attrd.get('class')
        if cls=='bk':
            m = self.color_re.search(style)
            if m:
                color = int(m.groups()[0],16)
            else:
                color = 0
            if(color!=0xFFFFFF):
                self.elts.append((y,x,BackgroundElt(color)))
        elif cls=='nu':
            self.active_elt = TextElt('')
            self.elts.append((y,x,self.active_elt))

    def handle_data(self,data):
        if self.active_elt:
            self.active_elt.text=data

    def handle_endtag(self,tag):
        self.active_elt = None

def parse_html_grid(text,border=True):
    p = _GridHTMLParser()
    if isinstance(text,bytes):
        text=text.decode()
    p.feed(text)
    return p.grid()
