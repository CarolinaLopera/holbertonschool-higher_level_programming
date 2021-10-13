#!/usr/bin/python3
'''This function create a object
of a Json file'''
import json

def load_from_json_file(filename):
    '''filename is the is the
    name to the json file'''
    with open(filename) as f:
        object = json.load(f)
        return object
