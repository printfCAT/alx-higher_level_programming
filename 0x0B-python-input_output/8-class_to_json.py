#!/usr/bin/python3
""" define a function """


def class_to_json(obj):
    """ JSON serializes a class object """
    return obj.__dict__
