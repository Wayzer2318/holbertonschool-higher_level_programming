#!/usr/bin/python3
""" inherit or instance """


def inherits_from(obj, a_class):
    """ inherit or instance """
    return type(obj) is not a_class and isinstance(obj, a_class)
