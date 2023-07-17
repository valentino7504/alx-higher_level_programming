#!/usr/bin/python3
'''

This module is used to test base.py and the Base class

'''


import unittest
import models.base


Base = models.base.Base


class TestBase(unittest.TestCase):
    """
    This tests the Base class in base.py and its functionality
    """
    def setUp(self) -> None:
        """
        sets up Base testing
        """
        Base.__nb_objects = 0

    def tearDown(self) -> None:
        """
        tearDown method for Base
        """
        Base.__nb_objects = 0

    def test_base_mod_docs(self):
        """
        test mod docs of the Base class
        """
        self.assertTrue(len(models.base.__doc__) > 1)

    def test_class_docs(self):
        """
        test documentation of the base class
        """
        self.assertTrue(len(Base.__doc__) > 1)

    def function_docs(self):
        """
        tests that methods have documentations
        """
        class_methods = [
            func for func in dir(models.base)
            if callable(getattr(Base, func))
            and not func.startswith("__")
        ]
        for func in class_methods:
            self.assertTrue(len(func) > 1)

    def test_id_given(self):
        """
        Tesing when the id is an int and given
        """
        base_with_id = Base(98)
        self.assertEqual(base_with_id.id, 98)

    def test_id_not_given(self):
        """
        Testing when the id is not given at all
        """
        base_without_id = Base()
        self.assertEqual(base_without_id.id, 1)

    def test_nb_instances(self):
        """
        Confirm that nb instances is private
        """
        new_base = Base(54)
        self.assertRaises(AttributeError, getattr, new_base, "__nb_objects")

    def test_negative_id(self):
        """
        tests for negative id
        """
        negative_base = Base(-12)
        self.assertTrue(negative_base.id == -12)

    def test_zero_id(self):
        """
        tests for zero id
        """
        zero_base = Base(0)
        self.assertEqual(zero_base.id, 0)

    def test_none_id(self):
        """
        Testing when the id is None
        """
        base_with_none = Base(None)
        self.assertEqual(base_with_none.id, 2)


if __name__ == "__main__":
    unittest.main()
