#!/usr/bin/python3
""" define a function """


def append_write(filename="", text=""):
    """ function that appends to a file """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
