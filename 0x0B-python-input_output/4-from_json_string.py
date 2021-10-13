#!/usr/bin/python3
'''This function return a Json
representation of a object'''
import json


def from_json_string(my_str):
    '''mi_str is the object (data structure)'''
    return json.loads(my_str)
