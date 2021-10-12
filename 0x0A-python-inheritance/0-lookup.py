#!/usr/bin/python3
'''This funtion print all attribites
of a class'''


def lookup(obj):
    '''obj is a class'''
    attributes = dir(obj)
    return attributes
