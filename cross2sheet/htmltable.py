"""
Reads grids that are formatted as HTML tables, provided a function that interprets style
information.
"""

import bisect, html.parser, re
from cross2sheet.grid_features import *

class _GridHTMLTableParser(html.parser.HTMLParser):

    def __init__(self,stylefunc):
        super().__init__()
        self.elts = []
        self.height = 0
        self.width = 0
        self.intd = False
        self.stylefunc=stylefunc

    def grid(self):
        g = Grid(self.height,self.width)
        g.features.extend(self.elts)
        return g

    def add_element(self,e):
        self.elts.append((self.row,self.col,e))
        if self.row>=self.height:
            self.height=self.row+1
        if self.col>=self.width:
            self.width=self.col+1

    def handle_starttag(self,tag,attrs):
        self.intd=False
        if tag=='table':
            self.row=-1
            self.col=-1
        if tag=='tr':
            self.row+=1
            self.col=-1
        elif tag=='td':
            self.col+=1
            self.intd=True
            for st in self.stylefunc(dict(attrs)):
                self.add_element(st)

    def handle_endtag(self,tag):
        if tag=='td':
            self.intd=False

    def handle_data(self,data):
        if self.intd:
            self.add_element(TextElt(data))

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
            if a in styledict:
                return [BackgroundElt(styledict[a])]
            else:
                return []
    p = _GridHTMLTableParser(stylefunc)
    p.feed(text)
    return p.grid()
