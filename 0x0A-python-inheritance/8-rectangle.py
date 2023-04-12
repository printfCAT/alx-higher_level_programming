#!/usr/bin/python3
""" define a class BaseGeometry """


class BaseGeometry:
    """ superclass BaseGeometry """
    pass

    def area(self):
        """ instance for calculating area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates if value parameter is int
            Args:
                name(str). a string input
                value(int). an integer input
         """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


""" define a subclass Rectangle """


class Rectangle(BaseGeometry):
    """ subclass Rectangle """

    def __init__(self, width, height):
        """
           Args:
                width(int). width of rectangle
                height(int). height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
