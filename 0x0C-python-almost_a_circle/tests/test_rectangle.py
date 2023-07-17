#!/usr/bin/python3
'''

This module is used to test the rectangle class


'''


import unittest
import io
import models.rectangle
import models.base
import unittest.mock


Base = models.base.Base
Rectangle = models.rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """
    This class tests the rectangle class
    """
    def setUp(self):
        """
        sets up for testing
        """
        Rectangle.__nb_objects = 0

    def tearDown(self):
        """
        tear down
        """
        Rectangle.__nb_objects = 0

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def assert_rect_stdout(self, rectangle: Rectangle, expected, mock_stdout):
        rectangle.display()
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_mod_docs(self):
        """
        Testing documentations for files
        """
        self.assertTrue(len(models.rectangle.__doc__) > 1)

    def test_class_docs(self):
        """
        Testing documentations for rcetangle class
        """
        self.assertTrue(len(Rectangle.__doc__) > 1)

    def test_func_docs(self):
        """
        Tests all functions in the rectangle class have docs
        """
        class_methods = [
            func for func in dir(Rectangle)
            if callable(getattr(Rectangle, func))
            and not func.startswith("__")
        ]
        for func in class_methods:
            self.assertTrue(len(func) > 1)

    def test_area(self):
        """
        tests if the area method is working
        """
        area_rectangle = Rectangle(4, 3, 0, 0, 224324235245)
        self.assertEqual(area_rectangle.area(), 12)

    def test_display(self):
        """
        tests if the display method is working
        """
        display_rectangle = Rectangle(2, 4, 0, 0, 83243545)
        self.assert_rect_stdout(display_rectangle, "##\n##\n##\n##\n")

    def test_distorted_display(self):
        """
        tests the offset display with x and y
        """
        display_second = Rectangle(3, 2, 1, 2, 7324)
        self.assert_rect_stdout(display_second, "\n\n ###\n ###\n")

    def test_height(self):
        """
        test setting up a rectangle with height
        """
        height_rect = Rectangle(4, 3, 5, 7, 802)
        self.assertEqual(height_rect.height, 3)

    def test_height_0(self):
        """
        tests when height is 0
        """
        with self.assertRaises(ValueError):
            _ = Rectangle(2, 0, 343, 22, 23)
        height_0 = Rectangle(12, 2, 3, 4, 92)
        self.assertRaises(ValueError, setattr, height_0, "height", 0)

    def test_height_less(self):
        """
        setting up a rectangle with height less than zero
        """
        with self.assertRaises(ValueError):
            _ = Rectangle(2, -3, 5, 7, 921)
        rect_less_height = Rectangle(2, 3, 4, 5, 55)
        self.assertRaises(ValueError, setattr, rect_less_height, "height", -2)
        rect_less_height2 = Rectangle(2, 3, 4, 5, 55)
        with self.assertRaises(ValueError):
            rect_less_height2.height = -3

    def test_height_notint(self):
        """
        rectangle with non int height
        """
        with self.assertRaises(TypeError):
            _ = Rectangle(2, 2.4, 6, 8, 10)
        with self.assertRaises(TypeError):
            _ = Rectangle(3, -1.6, 7, 9, 54)
        with self.assertRaises(TypeError):
            _ = Rectangle(5, [1, 2], 8, 7, 12)
        with self.assertRaises(TypeError):
            _ = Rectangle(3, None, 7, 8, 9)
        with self.assertRaises(TypeError):
            rect_no_height = Rectangle(3, 2, 4, 5, 7)
            rect_no_height.height = {"edwin", "mbony"}
        with self.assertRaises(TypeError):
            _ = Rectangle(2, 3.4, 1, 2, 1001)
        rect_no_height_2 = Rectangle(2, 3, 4, 5, 21982073)
        self.assertRaises(TypeError, setattr, rect_no_height_2,
                          "height", complex(2))

    def test_inheritance(self):
        """
        tests if rectangle inherits from base
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_private_height(self):
        """
        test if height is private
        """
        p_height_rect = Rectangle(2, 2, 3, 4, 5234343)
        self.assertRaises(AttributeError, getattr, p_height_rect, "__height")

    def test_private_width(self):
        """
        test if width is private
        """
        p_width_rect = Rectangle(2, 4, 6, 6, 46)
        self.assertRaises(AttributeError, getattr, p_width_rect, "__width")

    def test_private_x(self):
        """
        test if x is private
        """
        p_x_rect = Rectangle(2, 3, 4, 5, 8700)
        self.assertRaises(AttributeError, getattr, p_x_rect, "__x")

    def test_private_y(self):
        """
        test if y is private
        """
        p_y_rect = Rectangle(2, 3, 8, 9, 10424254657)
        self.assertRaises(AttributeError, getattr, p_y_rect, "__y")

    def test_arect_id(self):
        """
        checks the id of the rectangle
        """
        rectangle_id = Rectangle(2, 3, 6, 7, 90210)
        self.assertEqual(getattr(rectangle_id, "id"), 90210)

    def test_arect_no_id(self):
        """
        checks id with None id passed
        """
        rectangle_with_no_id = Rectangle(3, 5, 6, 7)
        self.assertEqual(getattr(rectangle_with_no_id, "id"), 1)
        rectangle_none_id = Rectangle(4, 5, 2, 13, None)
        self.assertEqual(getattr(rectangle_none_id, "id"), 2)

    def test_str(self):
        """
        test __str__ method for rectangle
        """
        rect_str = Rectangle(2, 3, 4, 5, 12345)
        string_check = "[Rectangle] (12345) 4/5 - 2/3"
        self.assertEqual(str(rect_str), string_check)
        self.assertEqual(rect_str.__str__(), string_check)

    def test_width(self):
        """
        initialising a rectangle with width
        """
        rect_width = Rectangle(13, 2, 3, 4, 5)
        self.assertEqual(rect_width.width, 13)
        rect_width.width = 11
        self.assertEqual(rect_width.width, 11)

    def test_width_0(self):
        """
        tests when width is 0
        """
        with self.assertRaises(ValueError):
            _ = Rectangle(0, 2, 3, 5, 72)
        with self.assertRaises(ValueError):
            _ = Rectangle(2, 3, 4, 5, 722)
            _.width = 0
        rect_0_width = Rectangle(2, 3, 4, 6, 922)
        self.assertRaises(ValueError, setattr, rect_0_width, "width", 0)

    def test_width_less(self):
        """
        rectangle with lower width
        """
        with self.assertRaises(ValueError):
            _ = Rectangle(-7, 8, 9, 8, 7)
        rect_less_width = Rectangle(3, 4, 5, 6, 10999)
        self.assertRaises(ValueError, setattr, rect_less_width, "width", -4)

    def test_width_notint(self):
        """
        rectangle with non int width
        """
        with self.assertRaises(TypeError):
            _ = Rectangle(2.4, 2, 6, 8, 1012)
        with self.assertRaises(TypeError):
            _ = Rectangle(-4.8, 7, 7, 9, 542)
        with self.assertRaises(TypeError):
            _ = Rectangle(complex(8, 4), 2, 23, 12, 111)
        with self.assertRaises(TypeError):
            _ = Rectangle({1, 2}, 5, 8, 7, 1233)
        with self.assertRaises(TypeError):
            _ = Rectangle(None, 7, 7, 8, 92121)
        with self.assertRaises(TypeError):
            rect_no_width = Rectangle(3, 2, 4, 5, 79854)
            rect_no_width.width = {"edwin", "mbony"}
        with self.assertRaises(TypeError):
            _ = Rectangle(2, 3.4, 1, 2, 1001)
        rect_no_width2 = Rectangle(2, 3, 4, 5, 21982073)
        self.assertRaises(TypeError, setattr,
                          rect_no_width2, "width", frozenset([1, 4]))

    def test_x(self):
        """
        rectangle with x
        """
        x_rectangle = Rectangle(4, 12, 8, 10, 42123)
        self.assertEqual(getattr(x_rectangle, "x"), 8)

    def test_x_0(self):
        """
        tests when x is 0
        """
        x_0 = Rectangle(1, 2, 0, 4, 1)
        self.assertEqual(getattr(x_0, "x"), 0)

    def test_x_less(self):
        """
        rectangle with invalid x value
        """
        with self.assertRaises(ValueError):
            _ = Rectangle(2, 3, -2, 4, 56732)
        with self.assertRaises(ValueError):
            _ = Rectangle(4, 9, -10, 23, 110)
        rect_x_less = Rectangle(5, 6, 7, 8, 9)
        self.assertRaises(ValueError, setattr, rect_x_less, "x", -5)

    def test_x_notint(self):
        """
        rectangle with nonint x
        """
        with self.assertRaises(TypeError):
            _ = Rectangle(3, 4, 4.8, 12, 202)
        with self.assertRaises(TypeError):
            _ = Rectangle(5, 8, [9, 5], 8, 11019)
        with self.assertRaises(TypeError):
            _ = Rectangle(3, 2, {"edwin": 8}, 9, 99199)

    def test_y(self):
        """
        rectangle with y
        """
        y_rectangle = Rectangle(3, 4, 5, 7, 2010)
        self.assertEqual(y_rectangle.y, 7)
        y_rectangle.y = 11
        self.assertEqual(y_rectangle.y, 11)

    def test_y_0(self):
        """
        y = 0 rectangle
        """
        rectangle_y0 = Rectangle(4, 7, 9, 0, 202)
        self.assertEqual(rectangle_y0.y, 0)

    def test_y_less(self):
        """
        rectangle with y less than required value
        """
        with self.assertRaises(ValueError):
            _ = Rectangle(4, 5, 6, -2, 102002)
        rectangle_y_2 = Rectangle(3, 4, 5, 7, 82828)
        self.assertRaises(ValueError, setattr, rectangle_y_2, "y", -9)

    def test_y_notint(self):
        """
        rectangle with non int y
        """
        with self.assertRaises(TypeError):
            _ = Rectangle(3, 4, 5, 3.2, 78)
        with self.assertRaises(TypeError):
            _ = Rectangle(3, 4, 5, {"hello": 2}, 9)
        rect_not_int_y = Rectangle(2, 3, 4, 5, 211)
        with self.assertRaises(TypeError):
            rect_not_int_y.y = [3, 5]
        rect_not_int_y2 = Rectangle(4, 5, 6, 7, 8)
        self.assertRaises(TypeError, setattr, rect_not_int_y2, "y", {2, 3})
        with self.assertRaises(TypeError):
            _ = Rectangle(4, 6, 2, (9, 8), 99)

    def test_update_args(self):
        """
        testing the update method with args
        """
        r1 = Rectangle(2, 3, 4, 5, 123)
        r1.update(7, 12, 13, 15, 16)
        r1_list = [r1.id, r1.width, r1.height, r1.x, r1.y]
        self.assertEqual(r1_list, [7, 12, 13, 15, 16])

    def test_one_arg(self):
        """
        tests when using only one arg
        """
        r_one = Rectangle(3, 7, 8, 10, 12)
        r_one.update(4)
        self.assertEqual(r_one.id, 4)
        self.assertEqual(r_one.width, 3)

    def test_update_kwargs(self):
        """
        testing the update method with kwargs
        """
        r2 = Rectangle(4, 5, 6, 7, 8)
        r2.update(id=6, width=8, height=12, x=1, y=1)
        r2_list = [r2.id, r2.width, r2.height, r2.x, r2.y]
        self.assertEqual(r2_list, [6, 8, 12, 1, 1])

    def test_update_mixed(self):
        """
        testing the update method with both kwargs and args
        """
        r3 = Rectangle(4, 8, 12, 1, None)
        r3.update(1201, 48, id=12, width=5, height=6, x=2, y=3)
        r3_list = [r3.id, r3.width, r3.height, r3.x, r3.y]
        self.assertEqual(r3_list, [1201, 48, 6, 2, 3])

        r4 = Rectangle(4, 7, 9, 10, 12)
        r4.update(99, id=4, x=1)
        self.assertEqual(r4.id, 99)
        self.assertEqual(r4.x, 1)

    def test_less_arguments(self):
        """
        testing with lower number of arguments
        """
        r5 = Rectangle(2, 2)
        r5_list = [r5.width, r5.height, r5.x, r5.y, r5.id]
        self.assertEqual(r5_list, [2, 2, 0, 0, 3])

    def test_onearg_creation(self):
        """tries to create a rectangle but is invalid"""
        with self.assertRaises(TypeError):
            _ = Rectangle(2)

    def test_noarg_creation(self):
        """
        tries to create a rectangle with no argument
        """
        with self.assertRaises(TypeError):
            _ = Rectangle()


if __name__ == "__main__":
    unittest.main()
