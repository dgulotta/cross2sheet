"""
Reads grids that are formatted as HTML tables, provided a function that interprets style
information.
"""

import bisect, re
from cross2sheet.grid_features import *
from bs4 import BeautifulSoup

class TableParser:

    def __init__(self):
        self.elts = []
        self.height = 0
        self.width = 0

    def grid(self):
        g = Grid(self.height,self.width)
        g.features.extend(self.elts)
        return g

    def add_element(self,y,x,e):
        self.elts.append((y,x,e))
        if y>=self.height:
            self.height=y+1
        if x>=self.width:
            self.width=x+1

    def parse(self,table,stylefunc):
        for y,row in enumerate(table.find_all('tr')):
            for x,elt in enumerate(row.find_all('td')):
                for st in stylefunc(elt.attrs):
                    self.add_element(y,x,st)
                if(elt.text):
                    self.add_element(y,x,TextElt(elt.text))

# TODO: add some way of picking out a particular table
def parse_html_table(text,stylefunc=None,styleattr=None,styledict=None):
    '''
    Parses an html table.

    The ``stylefunc`` function should be a function that takes a dictionary of
    ``<td>`` element attributes and returns a list of ``grid_features.GridFeature``
    objects that should be associated with that cell.
    '''
    if stylefunc is None:
        if styleattr is None:
            raise ValueError('Either stylefunc or styleattr is required')
        def stylefunc(attrs):
            a = attrs.get(styleattr)
            if isinstance(a,list):
                a=' '.join(a)
            if a in styledict:
                return [BackgroundElt(styledict[a])]
            else:
                return []
    soup=BeautifulSoup(text)
    parser=TableParser()
    for table in soup.find_all('table'):
        parser.parse(table,stylefunc)
    return parser.grid()
