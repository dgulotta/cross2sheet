#!/usr/bin/python

import argparse
import urllib.request
from cross2sheet.excel import save_xlsx
from cross2sheet.html14 import parse_html_grid
from cross2sheet.htmltable import parse_html_table
from cross2sheet.transforms import autonumber, outside_bars

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

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Convert a crossword to a spreadsheet.')
    parser.add_argument('input_file_or_url',type=str)
    parser.add_argument('output_file',type=str)
    parser.add_argument('--detect-background',type=bool,default=True)
    # Detecting bars in crosswords without them appears to be
    # harmless, as bars just get added between dark squares
    parser.add_argument('--detect-bars',type=boolean_arg,default=True)
    parser.add_argument('--autonumber',type=boolean_arg)
    parser.add_argument('--autonumber-cells-with-text',type=boolean_arg,default=False)
    parser.add_argument('--ocr-text',type=boolean_arg,default=False)
    parser.add_argument('--number-in-comment',type=boolean_arg,default=True)
    parser.add_argument('--number-in-cell',type=boolean_arg,default=True)
    parser.add_argument('--outer-border',type=boolean_arg,default=True)
    parser.add_argument('--color-attribute',type=str)
    parser.add_argument('--color-value-dark',type=str)
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
