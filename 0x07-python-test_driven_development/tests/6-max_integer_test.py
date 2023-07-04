#!/usr/bin/python3
"""
Module to test the max integer function
Based off unittest module and built using a
custom class
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ascending_lists(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2]), 2)

    def test_max_integer_raises(self):
        self.assertRaises(TypeError, max_integer, 5)
        self.assertRaises(KeyError, max_integer, {"Edwin": 23})
        self.assertRaises(TypeError, max_integer, [[1, 2, 3, 4], 6])
        self.assertRaises(TypeError, max_integer, 4.923)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_values(self):
        self.assertEqual(max_integer([-4566, -8, -9, -24, -76]), -8)
        self.assertEqual(max_integer([-6, -8, -9, 0, -12]), 0)

    def test_unordered_lists(self):
        self.assertEqual(max_integer([-6, 1, 12, 3, -5, -4, -9]), 12)

    def test_floats(self):
        self.assertEqual(max_integer([4.87, 3.28, -2.48, 7.93, 5.42]), 7.93)

    def test_mixed_values(self):
        self.assertEqual(max_integer([4.2, -4, 8, 10]), 10)

    def test_one_value(self):
        self.assertEqual(max_integer([66]), 66)

    def test_strings(self):
        self.assertEqual(max_integer("edwinmbonyade"), "y")
        self.assertEqual(max_integer("zyzyzz    yzyzzz"), "z")

    def test_empty_strings(self):
        self.assertEqual(max_integer(""), None)

    def test_multiple_words(self):
        self.assertEqual(max_integer(["wade", "in", "the", "water"]), "water")
        self.assertEqual(max_integer(["ade", "Edwin", "edwin"]), "edwin")

    def test_descending_lists(self):
        self.assertEqual(max_integer([10, 8, 5, 8]), 10)


if __name__ == "__main__":
    unittest.main()
