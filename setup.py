# -*- coding: utf-8 -*-
"""
Setup file for the packaging of the app
"""

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Uses PBR that is an easier method for maintainability purposes
setup(
    setup_requires=['pbr', 'PyYAML>=3.11', 'future>=0.16.0'],
    pbr=True,
)
