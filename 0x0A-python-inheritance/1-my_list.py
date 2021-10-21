#!/usr/bin/python3
'''This class sorted a list
and later it is print'''


class MyList(list):
    '''list is the list to print'''

    def print_sorted(self):
        '''self is list'''
        print(sorted(self))
