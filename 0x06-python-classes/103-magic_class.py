#!/usr/bin/python3
'''Define a MagicClass'''
import math


class MagicClass:
    '''This class is a magic class to bytecode'''

    def __init__(self, radius=0):
        '''Inicialization of atributes'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        '''This method computes the area'''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        '''This method computes the circumference'''
        return 2 * math.pi * self.__radius
