"""
Converts grids to Excel format.
"""

from openpyxl import Workbook
from openpyxl.styles import Style, PatternFill
from openpyxl.styles.borders import Border, Side
from openpyxl.styles.colors import Color
from openpyxl.comments import Comment
import collections
from cross2sheet.grid_features import *

class _CellStyle:

    border_names = { 'L' : 'left', 'R' : 'right', 'T' : 'top', 'B' : 'bottom' }

    def __init__(self):
        self.color = None
        self.borders = set()

    def style(self):
        kwargs = {}
        if self.color is not None:
            kwargs['fill']=PatternFill(patternType='solid',fgColor=Color('FF%06x'%self.color))
        if self.borders:
            kwa = {}
            for b in self.borders:
                kwa[self.border_names[b]]=Side(style='thick')
            kwargs['border']=Border(**kwa)
        return Style(**kwargs)

def write_sheet(grid,ws,text_in_cells=True,text_in_comments=False,leave_white_blank=True):
    styles = collections.defaultdict(_CellStyle)
    for r,c,elt in grid.features:
        cell = ws.cell(row=r+1,column=c+1)
        if isinstance(elt,BackgroundElt):
            if not (elt.color==0xFFFFFF and leave_white_blank):
                styles[r,c].color=elt.color
        elif isinstance(elt,TextElt):
            if text_in_cells:
                cell.value=elt.text
            if text_in_comments:
                cell.comment=Comment(elt.text,'')
        elif isinstance(elt,BorderElt):
            styles[r,c].borders.update(elt.dirs)
    for (r,c),s in styles.items():
        ws.cell(row=r+1,column=c+1).style=s.style()
    for d in ws.column_dimensions.values():
        d.width=3

def to_openpyxl(grid,**kwargs):
    wb = Workbook()
    write_sheet(grid,wb.active,**kwargs)
    return wb

def to_openpyxl_multi(grids,**kwargs):
    wb = Workbook()
    wb.remove_sheet(wb.active)
    for grid in grids:
        ws = wb.create_sheet()
        write_sheet(grid,ws,**kwargs)
    return wb

def save_xlsx(grid,filename,**kwargs):
    return to_openpyxl(grid,**kwargs).save(filename)
