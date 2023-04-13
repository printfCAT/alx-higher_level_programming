#!/usr/bin/python3
""" define a function """
def write_file(filename="", text=""):
    """ function that writes to a file """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
