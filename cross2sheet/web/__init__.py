from flask import Flask, render_template, request, send_file, redirect, url_for
from cross2sheet.image import ImageGrid
from cross2sheet.web.render import Table
from cross2sheet.web.serial import TableData
from cross2sheet.web.download import form_data_to_excel
from urllib.request import urlopen
from urllib.error import URLError
from flask import flash
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH']=0x1000000

def check_urlopen():
    try:
        urlopen('http://www.example.com/')
        return True
    except URLError:
        return False

if 'URLOPEN_ENABLED' not in app.config:
    app.config['URLOPEN_ENABLED']=check_urlopen()

@app.route("/")
def select():
    return render_template('select.html')

@app.route("/view",methods=['POST'])
def display():
    try:
        if 'file' in request.files:
            data=request.files['file'].read()
        elif request.form['url'].startswith('http'):
            data=urlopen(request.form['url']).read()
        else:
            return redirect(url_for('select'))
        img=ImageGrid(data)
        dim=img.dimensions()
        if dim[0]<=0 or dim[1]<=0:
            return render_template('select.html',error_msg='Failed to recognize crossword grid.')
        d=TableData(img=img)
        t=Table(d)
        return render_template('convert.html',table=t,data=d.to_json())
    except ValueError:
        return render_template('select.html',error_msg='File format not recognized.')
    except URLError as e:
        return render_template('select.html',error_msg='Could not load url: {}.'.format(e.reason.strerror))

@app.route("/download",methods=['POST'])
def download():
    f=form_data_to_excel(request.form)
    return send_file(f,as_attachment=True,attachment_filename='grid.xlsx',mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == "__main__":
    app.run()
