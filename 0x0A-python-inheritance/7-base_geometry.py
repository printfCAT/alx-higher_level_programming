#!/usr/bin/python3
""" define a class BaseGeometry """


class BaseGeometry:
    """ superclass BaseGeometry """
    pass

    def area(self):
        """ instance for calculating area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates if value parameter is int """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
