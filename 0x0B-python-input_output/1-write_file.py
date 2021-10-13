#!/usr/bin/python3
'''This function write in file
Return the number of characteres write'''


def write_file(filename="", text=""):
    with open(filename, 'w+') as f:
        return f.write(text)
