#!/usr/bin/python3
""" define a function """


import json


def to_json_string(my_obj):
    """ returns JSON representation of a string """
    return json.dumps(my_obj)
