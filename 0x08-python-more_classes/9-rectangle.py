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

    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        val1 = rect_1.width * rect_1.height
        val2 = rect_2.width * rect_2.height
        if val1 >= val2:
            return rect_1
        else:
            return rect_2

    def square(cls, size=0):
        return Rectangle(cls, cls)
