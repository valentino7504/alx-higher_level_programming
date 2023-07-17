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
    def get_attr_list(self, square: Square):
        return [square.id, square.size, square.x, square.y]

    def setUp(self) -> None:
        """
        Setup method for testing
        """
        Square.__nb_objects = 0

    def tearDown(self) -> None:
        Square.__nb_objects = 0

    def test_square_mod_docs(self):
        """
        testing if the square module has docs
        """
        squaremod_docs = models.square.__doc__
        self.assertTrue(len(squaremod_docs) > 2)

    def test_square_docs(self):
        """
        testing if the square class has docs
        """
        square_docs = Square.__doc__
        self.assertTrue(len(square_docs) > 2)

    def test_smethod_docs(self):
        """
        test square method docs
        """
        squ_methods = [
            func for func in dir(Square)
            if callable(getattr(Square, func))
            and not func.startswith("__")
        ]
        for func in squ_methods:
            self.assertTrue(len(func.__doc__) > 2)

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

    def test_square_update_args(self):
        """
        tests the overloaded method
        """
        square_load = Square(8, 2, 2, 8)
        square_load.update(99, 2, 3, 4)
        square_attributes = [square_load.id, square_load.size,
                             square_load.x, square_load.y]
        self.assertEqual(square_attributes, [99, 2, 3, 4])

    def test_square_update_kwargs(self):
        """
        tests update with kwargs only
        """
        square_kwargs = Square(10, 2, 3, 5)
        square_kwargs.update(id=23, size=5, x=9, y=10)
        attributes = [
            square_kwargs.id, square_kwargs.size, square_kwargs.x,
            square_kwargs.y
        ]
        self.assertEqual(attributes, [23, 5, 9, 10])

    def test_mixed_update(self):
        """
        tests when update is mixed with kwargs and args
        """
        s1 = Square(1, 2, 3, 4)
        s1.update(4, 5, y=9, x=8)
        self.assertEqual(self.get_attr_list(s1), [4, 5, 8, 9])
        s2 = Square(3, 4, 5, 5)
        s2.update(8, 10, id=9, x=7, y=10)
        self.assertEqual(self.get_attr_list(s2), [8, 10, 7, 10])

    def test_lesser_args(self):
        """
        tests with lesser args
        """
        s3 = Square(8, 10, 11, 12)
        s3.update(2, 3)
        self.assertEqual(self.get_attr_list(s3), [2, 3, 10, 11])

    def test_lesser_kwargs(self):
        """
        tests with lesser kwargs
        """
        s4 = Square(9, 12, 14, 18)
        s4.update(x=2, y=3)
        self.assertEqual(self.get_attr_list(s4), [18, 9, 2, 3])

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
        with self.assertRaises(TypeError):
            _ = Square(4.5, 3, 4, 22)
        with self.assertRaises(TypeError):
            _ = Square([1, 2, 3], 22, 22, 22)
        with self.assertRaises(TypeError):
            _ = Square((4,), 6, 6, 8)
        with self.assertRaises(TypeError):
            _ = Square({3, 2}, 4, 3, 21)
        with self.assertRaises(TypeError):
            _ = Square(True, 6, 6, 9)
        with self.assertRaises(TypeError):
            _ = Square(None, 4, 5, 6)

    def square_dict(self):
        """
        tests the to dictionary method
        """
        square_to_dict = Rectangle(3, 4, 5, 6)
        square_dict = square_to_dict.to_dictionary()
        test_dict = {
            "size": 3,
            "x": 5,
            "y": 6,
            "id": 6
        }
        self.assertEqual(square_dict, test_dict)

    def square_dict_update(self):
        """
        tests the to_dictionary method after update
        """
        s8 = Square(6, 8, 2, 1)
        s8_dict = s8.to_dictionary()
        test_dictionary = {
            "size": 6,
            "x": 8,
            "y": 2,
            "id": 1
        }
        self.assertEqual(s8_dict, test_dictionary)
        new_values = [9, 12, 10, 1]
        s8.update(*new_values)
        attribute_list = ["id", "size", "x", "y"]
        s8_dict = s8.to_dictionary()
        for attribute, value in zip(attribute_list, new_values):
            test_dictionary[attribute] = value
        self.assertEqual(s8_dict, test_dictionary)


if __name__ == "__main__":
    unittest.main()
