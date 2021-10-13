#!/usr/bin/python3
'''Program to add all the arguments to a json file'''
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    object = load_from_json_file("add_item.json")
except FileNotFoundError:
    object = []
save_to_json_file(object, "add_item.json")

for i in range(1, len(argv)):
    object.append(argv[i])
save_to_json_file(object, "add_item.json")
