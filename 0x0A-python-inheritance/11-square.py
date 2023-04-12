#!/usr/bin/python3
""" define a sub subclass Square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ sub subclass Square """

    def __init__(self, size):
        """
            Args:
                size(int).size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ finds area of square """
        return self.__size ** 2

    def __str__(self):
        """ prints an instance of square """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
