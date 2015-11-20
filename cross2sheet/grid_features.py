"""
Defines elements that can appear in a grid.
"""

from inspect import Parameter, Signature

class Grid:

    def __init__(self,height,width):
        self.height=height
        self.width=width
        self.features=[]

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

class BackgroundElt(GridFeature):
    'The background color of the cell, in 8-bit RGB format'
    
    fields=['color']

    def __repr__(self):
        return 'BackgroundElt(0x%06x)'%self.color

class TextElt(GridFeature):
    'The text inside the cell'

    fields=['text']

class BorderElt(GridFeature):
    "The borders of the cell that should be drawn (some subset of 'LRTB')"
    
    fields=['dirs']

