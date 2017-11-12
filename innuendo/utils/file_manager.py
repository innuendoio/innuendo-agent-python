# -*- coding: utf-8 -*-
"""
Is on charge of manage the files (load, save, etc)
"""

# Backwards compatibility imports
from __future__ import absolute_import, division, print_function
from builtins import *

import yaml

def load_file(file_path):
    return open(file_path, 'r')

def load_yaml(path):
    stream = load_file(path)
    return yaml.load(stream)
