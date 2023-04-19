#!/usr/bin/python3
""" define a subclass """


from base import Base


class Rectangle(Base):
    """ subclass Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
           Args:
                width(int). width of the rectangle
                height(int). height of the rectangle
                x(int). position on x axis
                y. position on y axis
                id(int). identification number
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """ retrieve width variable """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width variable """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve height variable """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height variable """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ retrieve x variable """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x variable """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ retrieve y variable """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y variable """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ computes area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle in stdout """
        [print("") for i in range(0, self.__y)]
        for i in range(0, self.__height):
            [print(" ", end="") for j in range(0, self.__x)]
            [print("#", end="") for k in range(self.__width)]
            print("")

    def update(self, *args, **kwargs):
        """ updates the attributes """
        if len(args) > 0:
            arg_names = ["id", "width", "height", "x", "y"]
            for n in range(len(args)):
                setattr(self, arg_names[n], args[n])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns dict rep of rectangle """
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }

    def __str__(self):
        """ prints a rectangle instance """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)
