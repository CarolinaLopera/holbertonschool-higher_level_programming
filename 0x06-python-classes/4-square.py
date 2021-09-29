#!/usr/bin/python3
'''Class to Square'''


class Square:
    '''This class create a square'''

    @property
    def size(self):
        '''getter to retrieve the size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter to get the size'''
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        '''Inicialization of size'''
        self.__size = size

    def area(self):
        '''This method computes the area'''
        return self.__size * self.__size
