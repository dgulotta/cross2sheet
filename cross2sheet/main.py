#!/usr/bin/python

import argparse
import urllib.request
from cross2sheet.excel import save_xlsx
from cross2sheet.html14 import parse_html_grid
from cross2sheet.htmltable import parse_html_table
from cross2sheet.transforms import autonumber, outside_bars, pad

def read(string):
    if '://' in string:
        req=urllib.request.urlopen(string)
        data=req.read()
        req.close()
        return data
    else:
        with open(string,'rb') as f:
            return f.read()

class NotRecognized(Exception):
    pass

class ReadFailed(Exception):
    pass

def read_image(data,args):
    try:
        from cross2sheet.image import ImageGrid
    except ImportError as e:
        if e.name in ('cv2','numpy'):
            raise NotRecognized('Image detection disabled because the module %s was not found.'%e.name)
        else:
            raise e
    try:
        img=ImageGrid(data)
    except ValueError:
        raise NotRecognized
    grid=img.grid()
    if args.detect_background:
        grid.features.extend(img.read_background())
    if args.detect_bars:
        grid.features.extend(img.read_bars())
    if args.autonumber_cells_with_text:
        grid.features.extend(img.autonumber_if_text_found())
    if args.ocr_text:
        grid.features.extend(img.read_text_ocr())
    if args.autonumber is None:
        args.autonumber=not (args.autonumber_cells_with_text or args.ocr_text)
    return grid

def read_html(data,args):
    try:
        data=data.decode()
    except UnicodeDecodeError:
        raise NotRecognized
    if '<div class="bk"' in data:
        return parse_html_grid(data)
    elif '<table' in data:
        if not args.color_attribute:
            raise NotRecognized('HTML contains a table, but --color-attribute not specified.  Try specifying --color-attribute and --color-value-dark.')
        return parse_html_table(data,styleattr=args.color_attribute,styledict={args.color_value_dark:0})
    else:
        raise NotRecognized

def read_data(data,args):
    errors = []
    for fn in (read_image,read_html):
        try:
            return fn(data,args)
        except NotRecognized as e:
            errors.extend(e.args)
    msg='Error: file format not recognized.  If the grid is an HTML file, try taking a screenshot.  If the grid is an image file, try converting it to PNG format.'
    if errors:
        msg='%s\nThe following warnings were encountered:\n%s'%(msg,'\n'.join(errors))
    raise ReadFailed(msg)

def process(grid,args):
    if args.autonumber:
        grid.features.extend(autonumber(grid))
    if args.outer_border:
        grid.features.extend(outside_bars(grid))
    pad(grid,*args.padding)

def save(grid,args):
    save_xlsx(grid,args.output_file,text_in_cells=args.number_in_cell,text_in_comments=args.number_in_comment)

def boolean_arg(s):
    sl=s.lower()
    if sl in ['y','yes','t','true','1','on']:
        return True
    elif sl in ['n','no','f','false','0','off']:
        return False
    else:
        raise ValueError('Unrecognized value %s'%s)

class ToggleAction(argparse.Action):

    def __init__(self,*args,**kwargs):
        kwargs.setdefault('metavar','{y,n}')
        super().__init__(*args,**kwargs)

    def __call__(self,parser,namespace,values,option_string=None):
        setattr(namespace,self.dest,boolean_arg(values))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Convert a crossword to a spreadsheet.')
    parser.add_argument('input_file_or_url',type=str)
    parser.add_argument('output_file',type=str)
    parser.add_argument('--padding',type=int,nargs=2,default=(1,3),metavar=('ROWS','COLS'),help='The number of blank rows and columns to add on the top and left of the grid')
    parser.add_argument('--detect-background',action=ToggleAction,default=True,help='Determines whether to detect the background color of the cells.')
    # Detecting bars in crosswords without them appears to be
    # harmless, as bars just get added between dark squares
    parser.add_argument('--detect-bars',action=ToggleAction,default=True,help='Determines whether to detect the cell border is thick or thin.')
    parser.add_argument('--autonumber',action=ToggleAction,help='Determines whether clue numbers will automatically be added in the cells that would be expected to have them under the usual crossword numbering conventions.')
    parser.add_argument('--autonumber-cells-with-text',action=ToggleAction,default=False,help='Determines whether clue numbers will be added in sequential order in cells that appear to have text in them.  (This is not too reliable.)')
    parser.add_argument('--ocr-text',action=ToggleAction,default=False,help="Determines whether to use the 'tesseract' program to recognize clue numbers.  (This is very unreliable.)")
    parser.add_argument('--number-in-comment',action=ToggleAction,default=True,help='Determines whether to write the clue numbers in comments.  (A triangle will appear in the corner of the cell, and hovering over it will reveal the clue number.)')
    parser.add_argument('--number-in-cell',action=ToggleAction,default=True,help='Determines whether to write the clue numbers in the spreadsheet cells.')
    parser.add_argument('--outer-border',action=ToggleAction,default=True,help='Determines whether to draw a border around the outside of the grid.')
    parser.add_argument('--color-attribute',type=str,help='(HTML table input) The name of the attribute that determines whether the cell is light or dark.')
    parser.add_argument('--color-value-dark',type=str,help='(HTML table input) The value of the above attribute when the cell is dark.')
    args=parser.parse_args()
    data=read(args.input_file_or_url)
    try:
        grid=read_data(data,args)
    except ReadFailed as e:
        import sys
        print(e.args[0],file=sys.stderr)
        sys.exit(65)
    process(grid,args)
    save(grid,args)
