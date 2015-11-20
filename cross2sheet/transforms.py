import itertools
from cross2sheet.grid_features import *

def autonumber(grid):
    numbers = []
    filled = set()
    hbars = set()
    vbars = set()
    for r,c,e in grid.features:
        if isinstance(e,BackgroundElt):
            if e.color==0:
                filled.add((r,c))
        elif isinstance(e,BorderElt):
            if 'T' in e.dirs:
                hbars.add((r,c))
            if 'B' in e.dirs:
                hbars.add((r+1,c))
            if 'L' in e.dirs:
                vbars.add((r,c))
            if 'R' in e.dirs:
                vbars.add((r,c+1))
    left_blocked = lambda y,x: (x==0 or (y,x-1) in filled or (y,x) in vbars)
    right_blocked = lambda y,x: (x==grid.width-1 or (y,x+1) in filled or (y,x+1) in vbars)
    top_blocked = lambda y,x: (y==0 or (y-1,x) in filled or (y,x) in hbars)
    bottom_blocked = lambda y,x: (y==grid.height-1 or (y+1,x) in filled or (y+1,x) in hbars)
    n=itertools.count(1)
    for y in range(grid.height):
        for x in range(grid.width):
            if (y,x) in filled:
                continue
            if (left_blocked(y,x) and not right_blocked(y,x)) or (top_blocked(y,x) and not bottom_blocked(y,x)):
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
