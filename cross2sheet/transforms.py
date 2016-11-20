import itertools
from cross2sheet.grid_features import *
from cross2sheet.analysis import GridAnalyzer

def autonumber(grid):
    numbers = []
    analyzer = GridAnalyzer(grid)
    n=itertools.count(1)
    for y,x in analyzer.squares():
        if (y,x) in analyzer.filled:
            continue
        if (analyzer.left_blocked(y,x) and not analyzer.right_blocked(y,x)) or (analyzer.top_blocked(y,x) and not analyzer.bottom_blocked(y,x)):
            numbers.append((y,x,TextElt(str(next(n)))))
    return numbers

def _elt_xcoord(y,x,elt):
    if isinstance(elt,BorderElt) and frozenset(elt.dirs)==frozenset('L'):
        return x-1
    return x

def _elt_ycoord(y,x,elt):
    if isinstance(elt,BorderElt) and frozenset(elt.dirs)==frozenset('T'):
        return y-1
    return y

def outside_bars(grid):
    new_elts=[]
    for n in range(grid.height):
        new_elts.append((n,0,BorderElt('L')))
        new_elts.append((n,grid.width-1,BorderElt('R')))
    for n in range(grid.width):
        new_elts.append((0,n,BorderElt('T')))
        new_elts.append((grid.height-1,n,BorderElt('B')))
    return new_elts

def pad(grid,rows,cols):
    grid.height+=rows
    grid.width+=cols
    grid.features=[(y+rows,x+cols,e) for y,x,e in grid.features]
