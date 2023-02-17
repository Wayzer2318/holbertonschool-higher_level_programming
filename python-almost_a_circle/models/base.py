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

    @classmethod
    def create(cls, **dictionary):
        """ create """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load from file """
        fileN = cls.__name__ + ".json"
        try:
            with open(fileN, mode="r") as f:
                jsonS = f.read()
                dictionaryL = cls.from_json_string(jsonS)
                objL = [cls.create(**objD) for objD in dictionaryL]
                return objL
        except FileNotFoundError:
            return []
