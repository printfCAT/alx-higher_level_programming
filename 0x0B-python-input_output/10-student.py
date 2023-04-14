#!/usr/bin/python3
""" define a class """


class Student:
    """ superclass Student """
    def __init__(self, first_name, last_name, age):
        """
            Args:
                first_name(str). student's 1st name
                last_name(str). student's 2nd name
                age(int). student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary rep of student instance """
        if attrs is None:
            return {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age
                    }
        else:
            new_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    new_dict[key] = getattr(self, key)
            return new_dict
