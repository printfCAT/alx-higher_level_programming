#!/usr/bin/python3
""" test for square """


import io
import unittest
from unittest.mock import patch
from models.basee import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """ define unittests for square """

    def test_squareone(self):
        """ test 1 for square """
        s1 = Square(3, 1, 3)
        self.assertEqual(str(s1), "[Square] (3) 1/3 - 3")

    def test_squaretwo(self):
        """ test 2 for square """
        s1 = Square(3, 1, 3)
        expected_output = "\n\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            s1.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_squarethree(self):
        """ test 3 for square """
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_squarefour(self):
        """ test 4 for square """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (2) 0/0 - 5")

    def test_squarefive(self):
        """ test 5 for square """
        self.assertEqual(Square(5).size, 5)

    def test_updateone(self):
        """ test 1 for update """
        s1 = Square(5)
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

    def test_updatetwo(self):
        """ test 2 for update """
        s1 = Square(5)
        s1.update(id=89, size=7, x=12, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_todictionaryone(self):
        """ test 1 for to_dictionary """
        r1 = Square(10, 2, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(str(r1_dictionary), "{'id': 6, 'size': 10, 'x': 2, 'y': 1}")

    def test_todictionarytwo(self):
        """ test 1 for to_dictionary """
        r1 = Square(10, 2, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(str(type(r1_dictionary)), "<class 'dict'>")


if __name__ == "__main__":
    """ main function """
    unittest.main()
