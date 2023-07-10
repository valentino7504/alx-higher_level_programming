#!/usr/bin/python3
"""

this module defines a rectangle class for use
in 0x0A

"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is  a rectangle class with various methods
    """
    def __init__(self, width, height) -> None:
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
