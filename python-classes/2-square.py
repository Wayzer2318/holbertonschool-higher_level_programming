#!/usr/bin/python3
""" square """


class Square:
    """ square """
    def __init__(self, name):
        self._Square__size = name
    
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

