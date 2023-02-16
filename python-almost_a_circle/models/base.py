#!/usr/bin/python3
""" Base """
import json


class Base:
    """ private class atribute """
    __nb_object = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    def to_json_string(list_dictionaries):
        """ to json """
        if list_dictionaries:
            return (json.dumps(list_dictionaries))
        else:
            return ("[]")
