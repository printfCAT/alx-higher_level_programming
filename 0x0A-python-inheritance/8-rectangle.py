#!/usr/bin/python3
""" define a class BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
