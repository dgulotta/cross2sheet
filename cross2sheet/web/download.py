from cross2sheet.web.serial import TableData
from cross2sheet.grid_features import Grid
from cross2sheet.transforms import autonumber, outside_bars
from cross2sheet.excel import to_openpyxl
from io import BytesIO

def form_data_to_excel(form):
    td=TableData.from_json(form['data'])
    g=Grid(td.height,td.width)
    if 'back' in form:
        g.features.extend(td.back)
    if 'bar' in form:
        g.features.extend(td.bars)
    if form['auto']=='auto':
        g.features.extend(autonumber(g))
    elif form['auto']=='text':
        g.features.extend(td.text)
    g.features.extend(outside_bars(g))
    i=BytesIO()
    to_openpyxl(g,text_in_cells='cells' in form,text_in_comments='comments' in form).save(i)
    i.seek(0)
    return i
