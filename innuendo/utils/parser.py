# -*- coding: utf-8 -*-

# Backwards compatibility imports
from __future__ import absolute_import, division, print_function
from builtins import *

from innuendo.core.exceptions import NotValidTypeException

# Native data types
_TYPES = {
    'int': int,
    'str': str,
    'bool': bool
}

def get_value_type(value):
    value = str(value.strip())
    
    if value not in _TYPES:
        raise NotValidTypeException(value=value)
    
    return _TYPES[value]