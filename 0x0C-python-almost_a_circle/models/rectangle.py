#!/usr/bin/python3
'''This is a class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''This class is inherited to Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
        elif value <= 0:
            raise ValueError("width must be > 0")

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
        elif value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        '''getter to retrieve the x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter to get the x'''
        self.__x = value
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        '''getter to retrieve the y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter to get the y'''
        self.__y = value
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        '''This method computes the area'''
        return self.__width * self.__height

    def display(self):
        '''This method prints a Rectangle with the character #'''
        for y in range(self.y):
            print()
        for i in range(self.__height):
            for x in range(self.x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        rectangle = '[Rectangle]' + ' (' + str(self.id) + ') '
        rectangle += str(self.x) + '/' + str(self.y) + ' - '
        rectangle += str(self.__width) + '/' + str(self.__height)
        return rectangle
