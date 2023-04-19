#!/usr/bin/python3
""" define a sub subclass """


from rectangle import Rectangle


class Square(Rectangle):
    """ a sub subclass Square """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Args:
                size(int). size of square
                x(int). position on x axis
                y(int). position on y axis
                id(int). identification number
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ retrieves size """
        return self.width

    @size.setter
    def size(self, value):
        """ initializes size """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width should be >= 0")
        self.width = value

    def update(self, *args, **kwargs):
        """ updates the attributes """
        if len(args) > 0:
            arg_names = ["id", "size", "x", "y"]
            for n in range(len(args)):
                setattr(self, arg_names[n], args[n])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns dict rep of square """
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """ prints a square instance """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
