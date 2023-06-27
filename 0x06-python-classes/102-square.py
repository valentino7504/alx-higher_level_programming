#!/usr/bin/python3
"""A square with getter and setter for size"""


class Square:
    """a square class with getter and setter"""
    def __init__(self, size=0) -> None:
        self.size = size

    @property
    def size(self):
        """returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets the size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.size ** 2

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Square):
            return self.area() == __value.area()
        return NotImplemented

    def __ne__(self, __value: object) -> bool:
        if isinstance(__value, Square):
            return self.area() != __value.area()
        return NotImplemented

    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, Square):
            return self.area() < __value.area()
        return NotImplemented

    def __gt__(self, __value: object) -> bool:
        if isinstance(__value, Square):
            return self.area() > __value.area()
        return NotImplemented

    def __le__(self, __value: object) -> bool:
        if isinstance(__value, Square):
            return self.area() <= __value.area()
        return NotImplemented

    def __ge__(self, __value: object) -> bool:
        if isinstance(__value, Square):
            return self.area() >= __value.area()
        return NotImplemented
