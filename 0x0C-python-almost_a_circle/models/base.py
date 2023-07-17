#!/usr/bin/python3
'''
This module is used to define the base class
'''


import json


class Base:
    """
    This class defines a base class
    """
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """
        Initialises the Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: list):
        """
        Returns the json string of a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0 or\
           type(list_dictionaries) != list:
            return "[]"
        return json.dumps(list_dictionaries)
