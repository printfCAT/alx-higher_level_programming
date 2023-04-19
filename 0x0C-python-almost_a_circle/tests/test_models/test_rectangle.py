#!/usr/bin/python3
""" unittest for rectangle """


import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ define unittestss for rectangle """

    def test_twoInputs(self):
        """ test for when the arguments passed are only 2 """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id-1)

    def test_fiveInputs(self):
        """ test for when the arguments passed are 5 """
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_stringinit(self):
        """ test for when input is string """
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_negativeinit(self):
        """ test for when input is negative """
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_dictinit(self):
        """ test for when input is a dict """
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {})

    def test_areatwoInputs(self):
        """ test for when arguments are only 2 """
        self.assertTrue(Rectangle(3, 2).area, 6)

    def test_areafiveInputs(self):
        """ test for when arguments are 5 """
        self.assertTrue(Rectangle(8, 7, 0, 0, 12).area, 56)

    def test_displaytwoInputs(self):
        """ test for when arguments are only 2 """
        expected_output = "###\n###\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            Rectangle(3, 2).display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_displayfiveInputs(self):
        """ test for when arguments are 5 """
        expected_output = "######\n######\n######\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            Rectangle(6, 3, 0, 0, 12).display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_displayfourInputs(self):
        """ test for when arguments are 4 """
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            Rectangle(2, 3, 2, 2).display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_strfiveInputs(self):
        """ test for __str__ output 5 arguments """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_strthreeInputs(self):
        """ test for __str__ output 3 arguments """
        r1 = Rectangle(5, 5, 1)
        self.assertEqual(str(r1), "[Rectangle] (4) 1/0 - 5/5")

    def test_updateone(self):
        """ test 1 for update """
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (10) 10/10 - 10/10")

    def test_updatetwo(self):
        """ test 2 for update """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_updatethree(self):
        """ test 3 for update """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_updatefour(self):
        """ test 4 for update """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

    def test_updatefive(self):
        """ test 5 for update """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

    def test_updatesix(self):
        """ test 6 for update """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_updateseven(self):
        """ test 7 for update """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (10) 10/10 - 10/1")

    def test_updateeight(self):
        """ test 8 for update """
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(y=1, x=3, width=2, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/10")

    def test_todictionaryone(self):
        """ test 1 for to_dictionary """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(str(r1_dictionary), "{'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9}")

    def test_todictionarytwo(self):
        """ test 2 for to_dictionary """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(str(type(r1_dictionary)), "<class 'dict'>")


if __name__ == "__main__":
    """ main function """
    unittest.main()
