#!/usr/bin/python3
""" Unittests for base """


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ define unittests for base """

    def test_idisNone(self):
        """ test when id input is None """
        self.assertEqual(Base().id, 1)

    def test_idisnotNone(self):
        """ test when id input is not None """
        self.assertEqual(Base(12).id, 12)

if __name__ == "__main__":
    """ main function """
    unittest.main()
