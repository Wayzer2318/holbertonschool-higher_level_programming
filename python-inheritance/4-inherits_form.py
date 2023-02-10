#!/usr/bin/python3
""" inherit or instance """


def inherits_form(obj, a_class):
    """ inherit or instance """
    return type(obj) is not a_class and isinstance(obj, a_class)
