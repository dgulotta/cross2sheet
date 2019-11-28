cross2sheet [![Build Status](https://travis-ci.org/dgulotta/cross2sheet.svg?branch=master)](https://travis-ci.org/dgulotta/cross2sheet)
===========

Features
========
The program reads a crossword grid and converts it into a spreadsheet.

Supported input formats:
* image files (any format supported by OpenCV or ImageMagick)
* html, in the format that was used in the 2014-2015 MIT Mystery Hunts (see for example http://web.mit.edu/puzzle/www/2014/puzzle/sledgehammered/)
* html tables, if the style information is encoded in a sufficiently simple way

Supported output formats:
* xlsx

Installing
==========

To install the required dependencies, run
```
pip install -e .[web]
```
You can remove the `web` option if you don't want to use the web interface.

Web interface
=============

Cross2sheet can be used via a web interface, as a command line program, or
as a library.  The web interface is the easiest to use.  The code for the web
interface can be found in the `cross2sheet/web` directory.

To test the web interface locally:
```
export FLASK_APP=cross2sheet/web/__init__.py
flask run
```

Instructions for deploying Flask applications can be found at
https://flask.palletsprojects.com/en/1.1.x/deploying/.

Command line interface
======================

The `cross2sheet.main` module includes a command line program that will
hopefully work most of the time.  For example, you can try the following:
```
python3 -m cross2sheet.main http://web.mit.edu/puzzle/www/2014/puzzle/puzzle_with_answer_nowhere_man/grid.png nowhere_man.xlsx
python3 -m cross2sheet.main http://web.mit.edu/puzzle/www/2015/puzzle/rid_fill/ rid_fill.xlsx
```
To see the full list of options supported by the program, run `python3 -m cross2sheet.main -h`.

API
===

The API is not particularly well documented, but there are some examples
in `cross2sheet/examples/examples.py`.
