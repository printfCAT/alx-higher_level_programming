#!/usr/bin/python3
""" define a function """


import json


def save_to_json_file(my_obj, filename):
    """ save JSON string to a file """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
