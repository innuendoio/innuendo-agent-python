# Backwards compatibility imports
from __future__ import print_function
from builtins import list

import unittest, os, future, filecmp
from innuendo.utils import file_manager as fm

class FileManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.path = str(os.path.dirname(os.path.abspath(__file__)))
        self.dir = 'files'
        self.files = ['test_load_small.txt', 'test_load_medium.txt', 'test_load_large.txt']

    def test_load_file_equals(self):
        for f in self.files:
            file_path = '{}/{}/{}'.format(self.path, self.dir, f)

            # Files content
            validate = fm.load_file(file_path).read()
            control = open(file_path, 'r').read()

            self.assertTrue(validate == control, 
                'Information loaded is not correct, expected value for {} is not the same as the one loaded'.format(f))
    
