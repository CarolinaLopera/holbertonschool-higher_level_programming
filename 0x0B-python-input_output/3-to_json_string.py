#!/usr/bin/python3
# get module
import json
'''This function return a Json
representation of a string'''


def to_json_string(my_obj):
    '''mi_obj is the object (string)'''
    return json.dumps(my_obj)
