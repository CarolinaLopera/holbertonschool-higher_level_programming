#!/usr/bin/python3
'''
This function add two integers
a must be an integer
b must be an integer
'''


def add_integer(a, b=98):
    '''
    sum a and b
    '''
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
