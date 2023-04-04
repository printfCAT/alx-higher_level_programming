#!/usr/bin/python3
"""define a class Rectangle"""


class Rectangle:
    """represent a Rectangle"""
    pass

    def __init__(self, width=0, height=0):
        """initialize a new Rectangle
        Args:
            width (int). width of the new rectangle
            height (int). height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set width of the new rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set height of the new rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """finds area of new rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """finds perimeter of new rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """prints a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """returns a string rep of a rectangle"""
        return "Rectangle({}, {})". format(self.__width, self.__height)
