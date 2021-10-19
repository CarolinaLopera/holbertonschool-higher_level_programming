#!/usr/bin/python3
'''This is a class Base'''


class Base:
    '''This class is the base of the poryect'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialization to attributes'''
        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
