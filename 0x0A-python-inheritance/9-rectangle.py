#!/usr/bin/python3
""" define a subclass """


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

    def area(self):
        """ finds area of Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ prints an instance of Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
