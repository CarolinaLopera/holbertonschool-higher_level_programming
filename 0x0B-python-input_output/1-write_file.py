#!/usr/bin/python3
'''This function write in file
Return the number of characteres write'''


def write_file(filename="", text=""):
    '''filename is the name of the file
    text is a string to write'''
    with open(filename, 'w+') as f:
        return f.write(text)
