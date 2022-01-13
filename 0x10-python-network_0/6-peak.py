#!/usr/bin/python3
'''This is my function'''


def find_peak(list_of_integers):
    '''Order a list and return the greater number'''
    if len(list_of_integers) == 0:
        return None
    order_list = sorted(list_of_integers)
    return order_list[-1]
