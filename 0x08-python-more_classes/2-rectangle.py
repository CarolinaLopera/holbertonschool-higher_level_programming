#!/usr/bin/python3
'''Class to Rectangle'''


class Rectangle:
    '''This class is create a rectangle'''

    def __init__(self, width=0, height=0):
        '''Inicialization of width and height'''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''getter to retrieve the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter to get the width'''
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        '''getter to retrieve the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter to get the height'''
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        '''This method computes the area'''
        return self.__height * self.__width

    def perimeter(self):
        '''This method computes the perimeter'''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
