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
