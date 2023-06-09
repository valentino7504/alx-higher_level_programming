#!/usr/bin/python3
"""defines a square class that can get area"""


class Square:
    """a square class with area method"""
    def __init__(self, size=0) -> None:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates area of the circle"""
        return (self.__size ** 2)
