#!/usr/bin/python3
""" define a class """


import json


class Base:
    """ superclass Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Args:
                id(int). integer counter for objects initialized
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns JSON string rep """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
