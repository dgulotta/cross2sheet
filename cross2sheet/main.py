#!/usr/bin/python

import argparse
import urllib.request
from cross2sheet.excel import save_xlsx
from cross2sheet.html14 import parse_html_grid
from cross2sheet.htmltable import parse_html_table
from cross2sheet.image import ImageGrid
from cross2sheet.transforms import autonumber, outside_bars

def read(string):
    if '://' in string:
        req=urllib.request.urlopen(string)
        data=req.read()
        req.close()
        return data
    else:
        return read('file://'+string)

class ReadFailed(Exception):
    pass

def read_image(data,args):
    try:
        img=ImageGrid(data)
    except ValueError:
        raise ReadFailed
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

def read_data(data,args):
    try:
        return read_image(data,args)
    except ReadFailed:
        pass
    data=data.decode()
    if '<div class="bk"' in data:
        return parse_html_grid(data)
    elif '<table' in data:
        if not args.color_attribute:
            raise ReadFailed('HTML contains a table, but --color-attribute not specified.  Try specifying --color-attribute and --color-value-dark, or taking a screenshot.')
        return parse_html_table(data,styleattr=args.color_attribute,styledict={args.color_value_dark:0})
    raise ReadFailed('File format not recognized.  If the grid is an HTML file, try taking a screenshot.  If the grid is an image file, try converting it to PNG format.')

def process(grid,args):
    if args.autonumber:
        grid.features.extend(autonumber(grid))
    if args.outer_border:
        grid.features.extend(outside_bars(grid))

def save(grid,args):
    save_xlsx(grid,args.output_file,text_in_cells=args.number_in_cell,text_in_comments=args.number_in_comment)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Convert a crossword to a spreadsheet.')
    parser.add_argument('input_file_or_url',type=str)
    parser.add_argument('output_file',type=str)
    parser.add_argument('--detect-background',type=bool,default=True)
    # Detecting bars in crosswords without them appears to be
    # harmless, as bars just get added between dark squares
    parser.add_argument('--detect-bars',type=bool,default=True)
    parser.add_argument('--autonumber',type=bool)
    parser.add_argument('--autonumber-cells-with-text',type=bool,default=False)
    parser.add_argument('--ocr-text',type=bool,default=False)
    parser.add_argument('--number-in-comment',type=bool,default=True)
    parser.add_argument('--number-in-cell',type=bool,default=True)
    parser.add_argument('--outer-border',type=bool,default=True)
    parser.add_argument('--color-attribute',type=str)
    parser.add_argument('--color-value-dark',type=str)
    args=parser.parse_args()
    data=read(args.input_file_or_url)
    try:
        grid=read_data(data,args)
    except ReadFailed as e:
        parser.error(e.args[0])
    process(grid,args)
    save(grid,args)