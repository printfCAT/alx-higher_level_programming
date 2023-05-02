#!/usr/bin/python3
""" Unitest for max_integer([...]) """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ define unittests for max_integer """

    def test_sortedList(self):
        """ test for sorted list """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsortedList(self):
        """ test for unsorted list """
        self.assertEqual(max_integer([3, 4, 1, 2]), 4)

    def test_emptyList(self):
        """ test for empty list """
        self.assertEqual(max_integer([]), None)

    def test_oneInput(self):
        """ test for one input """
        self.assertEqual(max_integer([4]), 4)

    def test_listofLists(self):
        """ test for list of lists """
        self.assertEqual(max_integer([[5, 6, 7, 8], [1, 2, 3, 4]]), [5, 6, 7, 8])

    def test_listofStr(self):
        """ test for list of strings """
        self.assertEqual(max_integer(["one", "two", "three", "four"]), 'two')

    def test_Listofdicts(self):
        """ test for list of dictionaries """
        with self.assertRaises(TypeError):
            max_integer([{"one": 1, "two": 2, "three": 3, "four": 4}, {"five": 5, "six": 6, "seven": 7, "eight": 8}])

    def test_dict(self):
        """test for dictionary """
        self.assertEqual(max_integer([{"one": 1, "two": 2, "three": 3, "four": 4}]), {'one': 1, 'two': 2, 'three': 3, 'four': 4})

    def test_float(self):
        """ test for list of floats """
        self.assertEqual(max_integer([0.1, 0.2, 0.3, 0.4]), 0.4)

    def test_negative(self):
        """ test for negative numbers """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_intsandfloats(self):
        """ test for list of int and floats """
        self.assertEqual(max_integer([1.5, 2, 0.3, -4]), 2)

    def test_string(self):
        """test for string """
        self.assertEqual(max_integer("name"), 'n')

    def test_emptyStr(self):
        """ test for empty string """
        self.assertEqual(max_integer(""), None)

if __name__ == "__main__":
    unittest.main()
