#!/usr/bin/python3
'''Class to Rectangle'''


class Rectangle:
    '''This class is create a rectangle'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Inicialization of width and height'''
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        '''Returns a new instance of Rectangle'''
        return (cls(size, size))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Define bigger or equal between two rectangles'''
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def area(self):
        '''This method computes the area'''
        return self.__height * self.__width

    def perimeter(self):
        '''This method computes the perimeter'''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        rectangle = []
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if (i + 1) != self.__height:
                rectangle.append('\n')
        return ("".join(rectangle))

    def __repr__(self):
        str = "Rectangle(" + repr(self.__width)
        str += ', ' + repr(self.__height) + ')'
        return str

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
