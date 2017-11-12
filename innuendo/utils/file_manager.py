# -*- coding: utf-8 -*-
"""
Is on charge of manage the files (load, save, etc)
"""

# Backwards compatibility imports
from __future__ import absolute_import, division, print_function
from builtins import *

import yaml

def load_file(file_path):
    """
    Returns a file given a path
    """
    return open(file_path, 'r')

def load_yaml(path):
    """
    Process a YAML file given a path and returns a dict with the data
    """
    stream = load_file(path)
    return yaml.load(stream)
