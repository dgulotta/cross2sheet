"""
Defines elements that can appear in a grid.
"""

from inspect import Parameter, Signature

class Grid:

    def __init__(self,height,width):
        self.height=height
        self.width=width
        self.features=[]

    def validate(self):
        if not (self.width in range(256) and self.height in range(7812)):
            raise ValueError
        if not all(self._valid_coords(r,c) and (e.validate() is None)
            for r,c,e in self.features):
            raise ValueError

    def _valid_coords(self,r,c):
        return r in range(self.height) and c in range(self.width)

class GridFeature:
    
    def _as_tuple(self):
        return tuple(getattr(self,f) for f in self.fields)

    def __init__(self,*args,**kwargs):
        sig = Signature([Parameter(f,Parameter.POSITIONAL_OR_KEYWORD) for f in self.fields])
        for k,v in sig.bind(*args,**kwargs).arguments.items():
            setattr(self,k,v)

    def __eq__(self,other):
        return type(self)==type(other) and self._as_tuple()==other._as_tuple()

    def __repr__(self):
        return '%s(%s)'%(type(self).__name__,','.join(repr(t) for t in self._as_tuple()))

    def __hash__(self):
        return hash(self._as_tuple())

    def validate(self):
        pass

class BackgroundElt(GridFeature):
    'The background color of the cell, in 8-bit RGB format'
    
    fields=['color']

    def validate(self):
        if self.color not in range(1<<24):
            raise ValueError

    def __repr__(self):
        return 'BackgroundElt(0x%06x)'%self.color

class TextElt(GridFeature):
    'The text inside the cell'

    def validate(self):
        if not isinstance(self.text,str):
            raise TypeError
        if len(self.text)>=256:
            raise ValueError

    fields=['text']

class BorderElt(GridFeature):
    "The borders of the cell that should be drawn (some subset of 'LRTB')"
    
    def validate(self):
        if not isinstance(self.dirs,str):
            raise TypeError
        if not (len(self.dirs)<=4 and self.dirs.isalpha()):
            raise ValueError

    fields=['dirs']

