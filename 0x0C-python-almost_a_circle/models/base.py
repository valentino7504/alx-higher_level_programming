#!/usr/bin/python3
'''
This module is used to define the base class
'''


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
