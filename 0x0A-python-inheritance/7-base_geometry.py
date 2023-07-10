#!/usr/bin/python3
"""
This module creates another geometry class
This time it has some other stuff
"""


class BaseGeometry:
    """This is a BaseGeometry class with area method"""

    def area(self):
        """
        validates area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates integers for BaseGeometry
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
