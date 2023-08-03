#!/usr/bin/python3
"""function"""


def inherits_from(obj, a_class):
    """function"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
