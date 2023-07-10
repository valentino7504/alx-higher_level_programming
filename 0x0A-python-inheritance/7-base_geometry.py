#!/usr/bin/python3
"""

This module creates a geometry class

"""


class BaseGeometry:
    """
    This is a BaseGeometry class with area method
    """
    def __init__(self) -> None:
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
