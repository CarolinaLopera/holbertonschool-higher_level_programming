#!/usr/bin/python3
'''Class to Square'''


class Square:
    '''This class have a size'''

    def __init__(self, size=0):
        '''This class raise error'''

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
