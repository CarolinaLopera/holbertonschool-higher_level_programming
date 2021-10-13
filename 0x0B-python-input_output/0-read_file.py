#!/usr/bin/python3
'''This function read a file
and it is write in the stdout'''


def read_file(filename=""):
    '''filename is de name of the file'''
    with open(filename) as f:
        read_file = f.read()
        print(read_file, end="")
