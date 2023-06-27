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

    def my_print(self):
        if self.size == 0:
            print()
        for _ in range(self.size):
            print("#"*self.size)
