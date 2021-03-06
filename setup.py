#!/usr/bin/env python
VERSION = "0.1.0"

from setuptools import find_packages, setup

setup(
    name="cross2sheet",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'numpy',
        'openpyxl',
        'opencv-python',
        'Wand',
    ],
    extras_require = {
        'web': ['Flask'],
    },
)
