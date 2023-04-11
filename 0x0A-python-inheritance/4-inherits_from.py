#!/usr/bin/python3
""" checks if object is an instance of a class\
    inherited directly from specified class
"""


def inherits_from(obj, a_class):
    """ the function to check """
    return issubclass(type(obj), a_class) and type(obj) != a_class
