"""
Reads grids that are formatted in HTML in the same way as those from the 2014-2015 MIT
Mystery Hunts (eg http://web.mit.edu/puzzle/www/2014/puzzle/sledgehammered/).
"""

import bisect, re
from cross2sheet.grid_features import *
from bs4 import BeautifulSoup

_coords_re = re.compile(r'left:(\d+)px;top:(\d+)px;')
_color_re = re.compile(r'border-top:#([0-9A-Fa-f]+)')

def _coords(style):
    x,y = _coords_re.search(style).groups()
    return (int(y),int(x))

def _color(style):
    m=_color_re.search(style)
    return int(m.groups()[0],16) if m else 0

def parse_html_grid(text):
    soup=BeautifulSoup(text)
    elts=[]
    xstartset=set()
    ystartset=set()
    for elt in soup.find_all('div',attrs={'class':'bk'}):
        y,x=_coords(elt.attrs['style'])
        col=_color(elt.attrs['style'])
        elts.append((y,x,BackgroundElt(col)))
        xstartset.add(x)
        ystartset.add(y)
    for elt in soup.find_all('div',attrs={'class':'nu'}):
        y,x=_coords(elt.attrs['style'])
        elts.append((y,x,TextElt(elt.text)))
    xstarts=sorted(xstartset)
    ystarts=sorted(ystartset)
    g=Grid(len(xstarts),len(ystarts))
    g.features=[(bisect.bisect_right(xstarts,x)-1,bisect.bisect_right(ystarts,y)-1,c) for y,x,c in elts]
    return g
