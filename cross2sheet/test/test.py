import unittest
from cross2sheet.grid_features import Grid, BackgroundElt, BorderElt, TextElt
from cross2sheet.image import ImageGrid
from cross2sheet.transforms import autonumber, outside_bars
from urllib.request import urlopen
from io import StringIO

def grid_to_string(g):
    i = StringIO()
    oldr=0
    for r,_,e in g.features:
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

def bars_to_string(g):
    ymax=g.height-1
    xmax=g.width-1
    grid=[[' ' for x in range(2*xmax+3)] for y in range(2*ymax+3)]
    for y,x,b in g.features:
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

def labels_to_string(g):
    grid=[['.' for x in range(g.width)] for y in range(g.height)]
    for y,x,t in g.features:
        if isinstance(t,TextElt):
            grid[y][x]='*'
    return '\n'.join(''.join(r) for r in grid)

def print_tests(url,grid):
    print('    url={}'.format(url))
    print('    rows={}'.format(grid.height))
    print('    cols={}'.format(grid.width))
    if any(isinstance(e,BackgroundElt) and e.color!=0xffffff for r,c,e in grid.features):
        print("    fill='''")
        print(grid_to_string(grid))
        print("'''")
    if any(isinstance(e,BorderElt) for r,c,e in grid.features):
        bordered=Grid(grid.height,grid.width)
        bordered.features.extend(grid.features)
        bordered.features.extend(outside_bars(grid))
        print("    bars='''")
        print(bars_to_string(bordered))
        print("'''")
    if any(isinstance(e,TextElt) for r,c,e in grid.features):
        label_str = labels_to_string(grid)
        gr = Grid(grid.height,grid.width)
        gr.features.extend(autonumber(gr))
        if label_str == labels_to_string(grid):
            print("    cells_with_text='auto'")
        else:
            print("    cells_with_text='''")
            print(label_str)
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
                grid=self.img.grid()
                grid.features.extend(self.img.read_background())
                f=grid_to_string(grid)
                self.assertEqual(self.fill.strip(),f.strip())
        if hasattr(self,'bars'):
            with self.subTest('bars'):
                grid=self.img.grid()
                grid.features.extend(self.img.read_bars())
                grid.features.extend(outside_bars(grid))
                b=bars_to_string(grid)
                self.assertEqual(self.bars.strip(),b.strip())
        if hasattr(self,'cells_with_text'):
            with self.subTest('cells_with_text'):
                if self.cells_with_text=='auto':
                    grid=self.img.grid()
                    grid.features.extend(self.img.read_background())
                    grid.features.extend(self.img.read_bars())
                    grid.features.extend(autonumber(grid))
                    self.cells_with_text=labels_to_string(grid)
                grid=self.img.grid()
                grid.features.extend(self.img.autonumber_if_text_found())
                t=labels_to_string(grid)
                self.assertEqual(self.cells_with_text.strip(),t.strip())
