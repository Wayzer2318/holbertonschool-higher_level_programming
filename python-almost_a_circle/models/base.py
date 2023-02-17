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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json """
        if list_dictionaries:
            return (json.dumps(list_dictionaries))
        else:
            return ("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """

        fileN = cls.__name__ + ".json"
        with open(fileN, mode="w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dictionaryL = [obj.to_dictionary() for obj in list_objs]
                jsonS = cls.to_json_string(dictionaryL)
                f.write(jsonS)

    @staticmethod
    def from_json_string(json_string):
        """ from json """

        if json_string is None:
            return []
        else:
            return json.loads(json_string)
