#!/usr/bin/python3
'''
This function prints a square.
Use character '#'
'size' is a size to square
'''


def print_square(size):
    '''
    size must be an positive integer
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        if (i + 1) != i:
            print()
