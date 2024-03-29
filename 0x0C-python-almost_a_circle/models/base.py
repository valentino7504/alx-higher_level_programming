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
    def load_from_file(cls):
        """
        returns a list of instances from a file
        """
        try:
            file = open(f"{cls.__name__}.json", "r", encoding="utf-8")
        except FileNotFoundError:
            return []
        list_input = file.read()
        list_dicts = cls.from_json_string(list_input)
        list_objs = [cls.create(**obj_dict) for obj_dict in list_dicts]
        file.close()
        return list_objs

    @classmethod
    def save_to_file(cls, list_objs: list):
        """
        Writes json representation to a file
        """
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            if list_objs is not None:
                dict_list = [item.to_dictionary() for item in list_objs]
                file.write(Base.to_json_string(dict_list))
            else:
                file.write("[]")

    @classmethod
    def create(cls, **dictionary):
        """
        creates an object
        """
        if cls.__name__ == "Square":
            dummy_obj = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy_obj = cls(1, 1)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @staticmethod
    def to_json_string(list_dictionaries: list):
        """
        Returns the json string of a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0 or\
           type(list_dictionaries) != list or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
