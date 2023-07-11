#!/usr/bin/python3
'''

This defines a student class with public attributes

'''


class Student:
    """
    Student class that has first_name, last_name attributes
    """

    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(attrs, list):
            return self.__dict__
        elif not all(isinstance(item, str) for item in attrs):
            return self.__dict__
        attr_dict = {}
        for item in attrs:
            new_item = self.__dict__.get(item, None)
            if new_item is not None:
                attr_dict[item] = new_item
        return attr_dict
