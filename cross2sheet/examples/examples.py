from urllib.request import urlopen
from cross2sheet.html14 import parse_html_grid
from cross2sheet.htmltable import parse_html_table
from cross2sheet.excel import save_xlsx, to_openpyxl_multi
from cross2sheet.image import ImageGrid
from cross2sheet.transforms import autonumber, outside_bars

def ridfill():
    req=urlopen('http://web.mit.edu/puzzle/www/2015/puzzle/rid_fill/')
    data=req.read()
    req.close()
    save_xlsx(parse_html_grid(data),'ridfill.xlsx')

def fill_in_the_blanks():
    req=urlopen('http://web.mit.edu/puzzle/www/2013/coinheist.com/get_smart/fill_in_the_blanks/index.html')
    data=req.read().decode()
    req.close()
    tables = data.split('</table>')
    grids=[parse_html_table(t,styleattr='class',styledict={'b':0}) for t in tables]
    to_openpyxl_multi(grids[:-1]).save('fill_in_the_blanks.xlsx')

def the_wicked_switch():
    req=urlopen('http://web.mit.edu/puzzle/www/2012/puzzles/a_circus_line/the_wicked_switch/1.png')
    data=req.read()
    req.close()
    img=ImageGrid(data)
    grid=img.grid()
    grid.features.extend(img.read_background())
    grid.features.extend(img.read_text_ocr())
    grid.features.extend(outside_bars(grid))
    save_xlsx(grid,'the_wicked_switch.xlsx')

def a_puzzle_with_answer_nowhere_man():
    req=urlopen('http://web.mit.edu/puzzle/www/2014/puzzle/puzzle_with_answer_nowhere_man/grid.png')
    data=req.read()
    req.close()
    img=ImageGrid(data)
    grid=img.grid()
    grid.features.extend(img.read_background())
    grid.features.extend(img.read_bars())
    grid.features.extend(outside_bars(grid))
    grid.features.extend(autonumber(grid))
    save_xlsx(grid,'nowhere_man.xlsx')
