import unittest
from cross2sheet.grid_features import BackgroundElt, BorderElt, TextElt
from cross2sheet.image import ImageGrid
from cross2sheet.transforms import autonumber, outside_bars
from urllib.request import urlopen
from io import StringIO

def grid_to_string(l):
    i = StringIO()
    oldr=0
    for r,_,e in l:
        if not isinstance(e,BackgroundElt):
            continue
        if r>oldr:
            oldr=r
            i.write('\n')
        if e.color==0:
            i.write('#')
        elif e.color==0xffffff:
            i.write('.')
        else:
            i.write('O')
    return i.getvalue()

def bars_to_string(l):
    ymax=max(y for y,_,_ in l)
    xmax=max(x for _,x,_ in l)
    grid=[[' ' for x in range(2*xmax+3)] for y in range(2*ymax+3)]
    for y,x,b in l:
        if not isinstance(b,BorderElt):
            continue
        for c in b.dirs:
            if c=='T':
                grid[2*y][2*x]='+'
                grid[2*y][2*x+1]='-'
                grid[2*y][2*x+2]='+'
            elif c=='L':
                grid[2*y][2*x]='+'
                grid[2*y+1][2*x]='|'
                grid[2*y+2][2*x]='+'
            elif c=='B':
                grid[2*y+2][2*x]='+'
                grid[2*y+2][2*x+1]='-'
                grid[2*y+2][2*x+2]='+'
            elif c=='R':
                grid[2*y][2*x+2]='+'
                grid[2*y+1][2*x+2]='|'
                grid[2*y+2][2*x+2]='+'
    return '\n'.join(''.join(r) for r in grid)

def labels_to_string(l):
    ymax=max(y for y,_,_ in l)
    xmax=max(x for _,x,_ in l)
    grid=[[' ' for x in range(xmax+1)] for y in range(ymax+1)]
    for y,x,t in l:
        if isinstance(t,TextElt):
            grid[y][x]='*'
    return '\n'.join(''.join(r) for r in grid)

def print_tests(grid):
    print('\trows={}'.format(grid.height))
    print('\tcols={}'.format(grid.width))
    if any(isinstance(e,BackgroundElt) and e.color!=0xffffff for r,c,e in grid.features):
        print("\tfill='''")
        print(grid_to_string(grid.features))
        print("'''")
    if any(isinstance(e,BorderElt) for r,c,e in grid.features):
        feat=list(grid.features)
        feat.extend(outside_bars(grid))
        print("\tbars='''")
        print(bars_to_string(feat))
        print("'''")
    if any(isinstance(e,TextElt) for r,c,e in grid.features):
        print("\tcells_with_text='''")
        print(labels_to_string(grid.features))
        print("'''")

class ImageTest(unittest.TestCase):

    def setUp(self):
        url=self.url
        if url.startswith('20'):
            url='http://web.mit.edu/puzzle/www/'+url
        req=urlopen(url)
        data=req.read()
        req.close()
        self.img=ImageGrid(data)
        self.maxDiff=None

    def test_all(self):
        detected=(len(self.img.breaks[0])-1,len(self.img.breaks[1])-1)
        expected=(self.rows,self.cols)
        self.assertEqual(expected,detected,'wrong dimensions')
        if hasattr(self,'fill'):
            with self.subTest('fill'):
                f=grid_to_string(self.img.read_background())
                self.assertEqual(self.fill.strip(),f.strip())
        if hasattr(self,'bars'):
            with self.subTest('bars'):
                grid=self.img.grid()
                grid.features.extend(self.img.read_bars())
                grid.features.extend(outside_bars(grid))
                b=bars_to_string(grid.features)
                self.assertEqual(self.bars.strip(),b.strip())
        if hasattr(self,'cells_with_text'):
            with self.subTest('cells_with_text'):
                if self.cells_with_text=='auto':
                    grid=self.img.grid()
                    grid.features.extend(self.img.read_background())
                    grid.features.extend(self.img.read_bars())
                    self.cells_with_text=labels_to_string(autonumber(grid))
                t=labels_to_string(self.img.autonumber_if_text_found())
                self.assertEqual(self.cells_with_text.strip(),t.strip())
