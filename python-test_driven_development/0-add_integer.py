#!/usr/bin/python3

def add_integer(a, b=98):
    if a is not int:
        raise TypeError('a must be an integer')
    if b is not int:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
