#!/usr/bin/python3
""" define a subclass """


class MyInt(int):
    """ subclass MyInt """
    def __eq__(self, another):
        """ reverses equal outcome """
        return super().__ne__(another)

    def __ne__(self, another):
        """ reverses not equal outcome """
        return super().__eq__(another)
