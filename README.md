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

A command line interface is planned.  In the meantime, there are some example
uses of the API in ```cross2sheet/examples/examples.py```.

Required software
=================
The code is written in Python 3.  It is tested with version 3.4 but might also
work with other versions.  The following modules are used:
* cv2, numpy : image input
* pyopenxl : xlsx output

The `tesseract` command line program can be used to read numbers in the grid, but in
most cases it is better to have cross2sheet guess where the numbers go.
