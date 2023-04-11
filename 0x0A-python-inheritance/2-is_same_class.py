#!/usr/bin/python3
""" checks if object is an instance of a class """


def is_same_class(obj, a_class):
    """ function that does the checking """
    if type(obj) == a_class:
        return True
    else:
        return False
