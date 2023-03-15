#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    key = str(key)
    new_dictionary = dict(a_dictionary)
    for i in a_dictionary:
        if i == key:
            del a_dictionary[key]
            return a_dictionary
        else:
            return new_dictionary
