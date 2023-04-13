#!/usr/bin/python3
""" define a function """


import json


def from_json_string(my_str):
    """ returns JSON string to object """
    return json.loads(my_str)
