# -*- coding: utf-8 -*-

# Backwards compatibility imports
from __future__ import absolute_import, division, print_function
from builtins import *

class InnuendoException(Exception):
    message = 'Internal server error'

    def __init__(self, message=None):
        if message:
            self.message = message

    def __str__(self):
        return str(self.message)

class NotValidTypeException(InnuendoException):
    message = 'The type %s is not a native python type'
    value = 'introduced'

    def __init__(self, message=None, value=None):
        if message:
            self.message = message
        if value:
            self.value = value

        self.message = self.message % (self.value)
