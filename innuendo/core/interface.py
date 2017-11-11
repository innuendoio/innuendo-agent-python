# -*- coding: utf-8 -*-

# Backwards compatibility imports
from __future__ import print_function
from builtins import dict
import future

# Imports
import sys, imp, os, argparse
from innuendo.utils import file_manager as fm
from innuendo.utils import parser

class TerminalInterface():
    
    def __init__(self):
        try:
            # Private constants for PATHs
            self._PATH = os.path.dirname(os.path.abspath(__file__))
            self._CONF_FOLDER_PATH = 'config'
            self._CONF_FILE_PATH = '{}/../{}/conf.yml'.format(self._PATH, self._CONF_FOLDER_PATH)
            
            # Loads a configuration file
            self.conf = fm.load_yaml(self._CONF_FILE_PATH)
            self.arguments = self.conf.get('arguments', dict())
            
        except IOError as e:
            print(e)
        except Exception as e:
            print(e)

    def process_args(self):
        arg_p = argparse.ArgumentParser()

        # Sets the arguments
        for k, v in self.arguments.items():
            arg_p.add_argument(k, help=v.get(
                'help', ''), type=parser.get_value_type(v.get('type', '')))

        args = arg_p.parse_args()
        print(args)
        print(args.command)

    def run(self):
        try:
            self.process_args()
                
            print('Run Forrest')
        except Exception as e:
            print(e)

