#!/usr/bin/python3
'''This function write a Json
representation of a object'''
import json


def save_to_json_file(my_obj, filename):
    '''mi_obj is the object to write'''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
