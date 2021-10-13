#!/usr/bin/python3
'''This function return a Json
representation of a string'''
import json


def to_json_string(my_obj):
    '''mi_obj is the object (string)'''
    return json.dumps(my_obj)
