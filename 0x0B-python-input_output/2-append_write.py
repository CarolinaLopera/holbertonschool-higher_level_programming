#!/usr/bin/python3
'''This function add on the file a string
Return the number of characteres added'''


def append_write(filename="", text=""):
    '''filename is the name of the file
    text is a string to add'''
    with open(filename, 'a+') as f:
        return f.write(text)
