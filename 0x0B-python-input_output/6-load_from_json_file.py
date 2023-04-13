#!/usr/bin/python3
""" define a function """


import json


def load_from_json_file(filename):
    """ creates object from JSON file """
    with open(filename, 'r') as f:
        return json.load(f)
