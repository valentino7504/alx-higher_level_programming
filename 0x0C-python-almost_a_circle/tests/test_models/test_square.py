#!/usr/bin/python3
'''

Testing the square class in this module

'''


import unittest
import models.base
import models.rectangle
import models.square
import unittest.mock


Base = models.base.Base
Rectangle = models.rectangle.Rectangle
Square = models.square.Square


class TestSquare(unittest.TestCase):
    """
    The unittest class to test the Square class
    """
    def setUp(self) -> None:
        """
        Setup method for testing
        """
        Square.__nb_objects = 0

    def tearDown(self) -> None:
        Square.__nb_objects = 0

    def test_square_inheritance(self):
        """
        checks to see if square inherits from rectangle
        """
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_square_attributes(self):
        """
        testing the getters for square attributes
        """
        square_att = Square(3, 4, 5, 6)
        self.assertEqual(square_att.size, 3)
        self.assertEqual(square_att.width, 3)
        self.assertEqual(square_att.height, 3)
        self.assertEqual(square_att.x, 4)
        self.assertEqual(square_att.y, 5)
        self.assertEqual(square_att.id, 6)
        square_att.update(4, width=2, height=2)
        self.assertEqual(square_att.width, 2)
        self.assertEqual(square_att.height, 2)
        self.assertEqual(square_att.id, 4)

    def test_square_id(self):
        """
        creates square with id
        """
        id_square = Square(6, 2, 2, 10)
        self.assertEqual(id_square.id, 10)

    def test_asquare_id(self):
        """
        checks to see if nb_objects functions correctly in Square
        """
        non_id_square = Square(5, 2, 2)
        self.assertEqual(non_id_square.id, 1)

    def test_none_id(self):
        """
        tests when id is none
        """
        none_id_square = Square(8, 9, 2, None)
        self.assertEqual(none_id_square.id, 2)

    def test_square_str(self):
        """
        Testing the __str__ method of the square class
        """
        str_square = Square(4, 5, 8, 10)
        self.assertEqual(str(str_square), "[Square] (10) 5/8 - 4")

    def test_square_size(self):
        """
        tests the square size attribute
        """
        square1 = Square(8, 2, 2, 20)
        self.assertEqual(square1.size, 8)
        self.assertEqual(square1.width, square1.size)
        self.assertEqual(square1.height, square1.size)

    def test_negative_size(self):
        """
        tests when the size attribute is less than 0
        """
        with self.assertRaises(ValueError):
            _ = Square(-2, 4, 4, 2)

    def test_zero_size(self):
        """
        tests for zero size
        """
        with self.assertRaises(ValueError):
            _ = Square(0, 3, 4, 5)
        square_zero = Square(3, 4, 5, 6)
        self.assertRaises(ValueError, setattr, square_zero, "size", 0)

    def test_nonint_size(self):
        """
        tests when the user tries to use a nonint size
        """


if __name__ == "__main__":
    unittest.main()
