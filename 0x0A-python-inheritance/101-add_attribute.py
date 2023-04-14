#!/usr/bin/python3
""" define a function """


def add_attribute(self, name, value):
    """ sets a new object attribute """
    if not hasattr(self, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(self, name, value)
