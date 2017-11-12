# -*- coding: utf-8 -*-
import yaml

def load_file(file_path):
    return open(file_path, 'r')

def load_yaml(path):
    stream = load_file(path)
    return yaml.load(stream)
