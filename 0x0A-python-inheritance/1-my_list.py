#!/usr/bin/python3
""" define a child class """


class MyList(list):
    """ represents a child class """

    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
