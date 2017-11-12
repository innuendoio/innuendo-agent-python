# Backwards compatibility imports
from __future__ import print_function
from builtins import list

import unittest, os, future, filecmp
from innuendo.utils import file_manager as fm
from yaml.scanner import ScannerError

class FileManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.path = str(os.path.dirname(os.path.abspath(__file__)))
        self.dir = 'files'
        self.files = ['test_load_small.txt', 'test_load_medium.txt', 'test_load_large.txt']

    def tearDown(self):
        self.files = list()

    def test_load_file_equals(self):
        for f in self.files:
            file_path = '{}/{}/{}'.format(self.path, self.dir, f)

            # Files content
            validate = fm.load_file(file_path).read()
            control = open(file_path, 'r').read()

            self.assertTrue(validate == control,
                'Information loaded is not correct, expected value for {} is not the same as the one loaded'.format(f))

    def test_load_file_size(self):
        self.files.extend(['test_load_xlarge.txt', 'test_load_xxlarge.txt'])

        for f in self.files:
            file_path = '{}/{}/{}'.format(self.path, self.dir, f)

            self.assertIsNotNone(fm.load_file(file_path).read(), 'There was an error during the loading of the file. It is possible to big for being processed')

    def test_load_yaml_is_good(self):
        files_good = ['test_load_yml_good_a.yml', 'test_load_yml_good_b.yml']

        for f in files_good:
            file_path = '{}/{}/{}'.format(self.path, self.dir, f)

            self.assertIsInstance(fm.load_yaml(file_path), dict, 'Error processing the YAML file, the result object is not a dict')

    def test_load_yaml_is_bad(self):
        files_good = ['test_load_yml_bad_a.yml', 'test_load_yml_bad_b.yml']

        for f in files_good:
            file_path = '{}/{}/{}'.format(self.path, self.dir, f)

            with self.assertRaises(ScannerError):
                fm.load_yaml(file_path)
