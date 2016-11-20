import itertools
from cross2sheet.grid_features import BackgroundElt, BorderElt

class GridAnalyzer:
    def __init__(self,grid):
        self.grid=grid
        self.filled=set()
        self.hbars=set()
        self.vbars=set()
        for r,c,e in grid.features:
            if isinstance(e,BackgroundElt):
                if e.color==0:
                    self.filled.add((r,c))
            elif isinstance(e,BorderElt):
                if 'T' in e.dirs:
                    self.hbars.add((r,c))
                if 'B' in e.dirs:
                    self.hbars.add((r+1,c))
                if 'L' in e.dirs:
                    self.vbars.add((r,c))
                if 'R' in e.dirs:
                    self.vbars.add((r,c+1))

    def is_blank(self,y,x):
        return (x>=0 and x<self.grid.width and y>=0 and y<self.grid.height
            and (y,x) not in self.filled)

    def left_blocked(self,y,x):
        return x==0 or (y,x-1) in self.filled or (y,x) in self.vbars

    def right_blocked(self,y,x):
        return (x==self.grid.width-1 or (y,x+1) in self.filled
            or (y,x+1) in self.vbars)

    def top_blocked(self,y,x):
        return y==0 or (y-1,x) in self.filled or (y,x) in self.hbars

    def bottom_blocked(self,y,x):
        return (y==self.grid.height-1 or (y+1,x) in self.filled
            or (y+1,x) in self.hbars)

    def word_length_horizontal(self,y,x):
        if not self.left_blocked(y,x):
            return None
        xn=x
        while not self.right_blocked(y,xn):
            xn=xn+1
        if xn==x and (y,x-1) not in self.filled and (y,x+1) not in self.filled:
            return None
        return xn-x+1

    def word_length_vertical(self,y,x):
        if not self.top_blocked(y,x):
            return None
        yn=y
        while not self.bottom_blocked(yn,x):
            yn=yn+1
        if yn==y and (y-1,x) not in self.filled and (y+1,x) not in self.filled:
            return None
        return yn-y+1

    def squares(self):
        return itertools.product(range(self.grid.height),
            range(self.grid.width))

    def word_lengths(self):
        lengths = []
        for y,x in self.squares():
            l = self.word_length_vertical(y,x)
            if l is not None:
                lengths.append(l)
            l = self.word_length_horizontal(y,x)
            if l is not None:
                lengths.append(l)
        return lengths

    def is_cheater(self,y,x):
        return ((y,x) in self.filled and
            (self.is_blank(y,x-1)^self.is_blank(y,x+1)) and
            (self.is_blank(y-1,x)^self.is_blank(y+1,x)))

    def connected_components(self):
        mark = set()
        n = 0
        for y,x in self.squares():
            if (y,x) in self.filled or (y,x) in mark:
                continue
            n += 1
            queue = []
            def push(yn,xn):
                if (yn,xn) not in mark:
                    mark.add((yn,xn))
                    queue.append((yn,xn))
            push(y,x)
            while queue:
                yy,xx = queue.pop()
                if not self.top_blocked(yy,xx):
                    push(yy-1,xx)
                if not self.bottom_blocked(yy,xx):
                    push(yy+1,xx)
                if not self.left_blocked(yy,xx):
                    push(yy,xx-1)
                if not self.right_blocked(yy,xx):
                    push(yy,xx+1)
        return n

    def badness(self):
        cheaters = sum(self.is_cheater(y,x) for y,x in self.squares())
        lengths = self.word_lengths()
        shorts = sum(1 for l in lengths if l<=2)
        extra_components = self.connected_components()-1
        return 30*extra_components+10*shorts+cheaters
