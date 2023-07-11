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

    def to_json(self):
        return self.__dict__
