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

    @classmethod
    def save_to_file(cls, list_objs: list):
        """
        Writes json representation to a file
        """
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            if list_objs is not None:
                file.write(Base.to_json_string(dict_list))
            else:
                dict_list = [item.to_dictionary() for item in list_objs]
                file.write("[]")

    @staticmethod
    def to_json_string(list_dictionaries: list):
        """
        Returns the json string of a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0 or\
           type(list_dictionaries) != list or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
