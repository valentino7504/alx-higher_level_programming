#!/usr/bin/python3
'''

This module is used to test base.py and the Base class

'''


import unittest
import models.base
import models.rectangle
import models.square
import json


Base = models.base.Base
Rectangle = models.rectangle.Rectangle
Square = models.square.Square


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
        self.assertEqual(negative_base.id, -12)

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

    def test_baseto_json_empty(self):
        """
        tests to_json on empty list
        """
        my_str = Base.to_json_string([])
        self.assertEqual(my_str, "[]")

    def test_baseto_json_none(self):
        """
        tests to_json on None
        """
        another_str = Base.to_json_string(None)
        self.assertEqual(another_str, "[]")

    def test_baseto_json(self):
        """
        tests the to_json method on actual dictionary
        """
        r_dict = Rectangle(10, 7, 2, 8, 5)
        dictionary_str = Base.to_json_string([r_dict.to_dictionary()])
        dict_list = [{"id": 5, "width": 10, "height": 7, "x": 2, "y": 8}]
        self.assertEqual(json.loads(dictionary_str), dict_list)

    def test_json_to_file(self):
        """
        tests adding json rep to file
        """
        list_objs = [Square(3, 4, 5, 2)]
        Square.save_to_file(list_objs)
        square_str = '[{"id": 2, "size": 3, "x": 4, "y":5}]'
        with open("Square.json", "r", encoding="utf-8") as file:
            line = file.readline()
        self.assertEqual(json.loads(line), json.loads(square_str))

    def test_empty_json_to_file(self):
        """
        tests empty json rep to file
        """
        list_obj2 = []
        Base.save_to_file(list_obj2)
        with open("Base.json", "r", encoding="utf-8") as file:
            line2 = file.readline()
        self.assertEqual(line2, "[]")

    def test_none_json_to_file(self):
        """
        tests empty json rep to file
        """
        list_obj3 = None
        Base.save_to_file(list_obj3)
        with open("Base.json", "r", encoding="utf-8") as file:
            line3 = file.readline()
        self.assertEqual(line3, "[]")

    def test_json_to_dict(self):
        """
        tests the from_json_string method
        """
        list_input = [{'id': 8, 'width': 19, 'height': 6}]
        json_string = Base.to_json_string(list_input)
        self.assertEqual(Base.from_json_string(json_string),
                         json.loads(json.dumps(list_input)))

    def test_njson_to_dict(self):
        """
        tests the from_json_string method
        """
        list_input = []
        json_string = Base.to_json_string(list_input)
        self.assertEqual(Base.from_json_string(json_string),
                         json.loads(json.dumps(list_input)))

    def test_none_to_dict(self):
        """
        tests the from_json_string method
        """
        list_input = None
        json_string = Base.to_json_string(list_input)
        self.assertEqual(Base.from_json_string(json_string), [])

    def test_rect_create(self):
        """
        tests the create method
        """
        create_dict = {'width': 22, 'height': 20, 'id': 8, 'x': 82, 'y': 19}
        new_rect = Rectangle.create(**create_dict)
        self.assertEqual(new_rect.id, 8)
        self.assertEqual(new_rect.width, 22)
        self.assertEqual(new_rect.height, 20)
        self.assertEqual(new_rect.x, 82)
        self.assertEqual(new_rect.y, 19)

    def test_rect_create(self):
        """
        tests the create method
        """
        create_dict = {'width': 22, 'height': 20, 'id': 8, 'x': 82, 'y': 19}
        new_rect = Rectangle.create(**create_dict)
        self.assertEqual(new_rect.id, 8)
        self.assertEqual(new_rect.width, 22)
        self.assertEqual(new_rect.height, 20)
        self.assertEqual(new_rect.x, 82)
        self.assertEqual(new_rect.y, 19)

    def test_square_create(self):
        """
        tests create method on Square
        """
        create_dict2 = {'size': 20, 'id': 8, 'x': 82, 'y': 19}
        new_rect = Square.create(**create_dict2)
        self.assertEqual(new_rect.id, 8)
        self.assertEqual(new_rect.size, 20)
        self.assertEqual(new_rect.x, 82)
        self.assertEqual(new_rect.y, 19)

    def test_sq_create_none(self):
        """
        tests create method with none
        """
        s8 = Square.create(**{})
        self.assertEqual(s8.size, 1)
        self.assertEqual(s8.x, 0)
        self.assertEqual(s8.y, 0)
        self.assertEqual(s8.id, 7)

    def test_sq_create_noargs(self):
        """
        tests create method with no args
        """
        s9 = Square.create()
        self.assertEqual(s9.size, 1)
        self.assertEqual(s9.x, 0)
        self.assertEqual(s9.y, 0)
        self.assertEqual(s9.id, 6)

    def test_sq_create_someargs(self):
        """
        tests create with some args
        """
        s10 = Square.create(**{"id": 12})
        self.assertEqual(s10.id, 12)
        self.assertEqual(s10.size, 1)
        self.assertEqual(s10.x, 0)
        self.assertEqual(s10.y, 0)

    def test_sload_files(self):
        """
        testing the loading from files
        """
        r_final = Rectangle(10, 2, 4, 5, 21)
        list_inp = [r_final]
        Rectangle.save_to_file(list_inp)
        del r_final
        s_final = Square(10, 4, 5, 21)
        list_inp2 = [s_final]
        Square.save_to_file(list_inp2)
        del s_final
        r_another = Rectangle.load_from_file()[0]
        s_another = Square.load_from_file()[0]
        r_list = [r_another.id, r_another.width, r_another.height,
                  r_another.x, r_another.y]
        s_list = [s_another.id, s_another.size, s_another.x,
                  s_another.y]
        self.assertEqual(s_list, [21, 10, 4, 5])


if __name__ == "__main__":
    unittest.main()
