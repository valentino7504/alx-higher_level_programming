#!/usr/bin/python3
"""
This module defines a square class based on
the rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This is a custom square class
    """
    def __init__(self, size) -> None:
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__width}/{self.__height}"
