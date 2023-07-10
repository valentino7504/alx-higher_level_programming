#!/usr/bin/python3
"""
This module creates another geometry class
This time it has some other stuff
It has integer validator methods
"""


class BaseGeometry:
    """
    This is a BaseGeometry class with area method
    """

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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
