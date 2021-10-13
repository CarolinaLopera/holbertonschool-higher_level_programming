#!/usr/bin/python3
'''This function write in file
Return the number of characteres write'''


def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        write_file = f.write(text)
        return write_file
