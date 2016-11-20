cross2sheet [![Build Status](https://travis-ci.org/dgulotta/cross2sheet.svg?branch=master)](https://travis-ci.org/dgulotta/cross2sheet)
===========

A program to convert crossword grids to spreadsheet format

Features
========
The program reads a crossword grid and converts it into a spreadsheet.

Supported input formats:
* image files (any format supported by OpenCV)
* html, in the format that was used in the 2014-2015 MIT Mystery Hunts (see for example http://web.mit.edu/puzzle/www/2014/puzzle/sledgehammered/)
* html tables, if the style information is encoded in a sufficiently simple way

Supported output formats:
* xlsx

The `cross2sheet.main` module includes a command line program that will
hopefully work most of the time.  For example, you can try the following:
```
python -m cross2sheet.main http://web.mit.edu/puzzle/www/2014/puzzle/puzzle_with_answer_nowhere_man/grid.png nowhere_man.xlsx
python -m cross2sheet.main http://web.mit.edu/puzzle/www/2015/puzzle/rid_fill/ rid_fill.xlsx
```
To see the full list of options supported by the program, run `python -m cross2sheet.main -h`.

The `cross2sheet.web` module provides a web interface.

There some example uses of the API in `cross2sheet/examples/examples.py`.

Required software
=================
The code is written in Python 3.  It is tested with version 3.4 but might also
work with other versions.  The following packages are used:
* OpenCV 3, NumPy : image input
* BeautifulSoup 4 : html input
* OpenPyXL : xlsx output
* Flask : web interface

The PyPI package for OpenCV seems not to work for everyone (at least it does
not work on my Gentoo system), and moreover setuptools won't recognize if you
have installed OpenCV some other way, so it is not listed as a required
dependency.  You can try to install the package by running `pip install
opencv-python`.

The `tesseract` command line program can be used to read numbers in the grid, but in
most cases it is better to have cross2sheet guess where the numbers go.
