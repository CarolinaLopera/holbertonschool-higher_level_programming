#!/usr/bin/python3
'''Class to Square'''


class Square:
    '''This class create a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Inicialization of size'''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''getter to retrieve the position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''setter to get the position'''
        self.__position = value
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''This method computes the area'''
        return self.__size * self.__size

    def my_print(self):
        '''This method print a squere in #'''
        self.square = self.__size
        if self.square == 0:
            print()
            return
        # [print("") for i in range(0, self.__position[1])]
        for j in range(0, self.__position[1]):
            print("")
        for i in range(self.square):
            for j in range(0, self.__position[0]):
                print(" ", end="")
                # else:
                #     print(" ", end="")
            for i in range(self.square):
                print("#", end="")
            print()
