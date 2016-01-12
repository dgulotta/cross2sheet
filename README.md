cross2sheet
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

There some example uses of the API in `cross2sheet/examples/examples.py`.

Required software
=================
The code is written in Python 3.  It is tested with version 3.4 but might also
work with other versions.  The following packages are used:
* OpenCV 3 : image input
* OpenPyXL : xlsx output

There is no PyPi package for OpenCV, so you will need to install it manually.

The `tesseract` command line program can be used to read numbers in the grid, but in
most cases it is better to have cross2sheet guess where the numbers go.
