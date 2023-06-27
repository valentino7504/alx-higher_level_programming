#!/usr/bin/python3
"""A square with getter and setter for size
Area and print methods also included"""


class Square:
    """a square class with getter, setter, printer and area method"""
    def __init__(self, size=0, position=(0, 0)) -> None:
        self.size = size
        self.position = position

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
        """returns the area"""
        return self.size ** 2

    def raise_pos_error(self):
        raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            self.raise_pos_error()
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            self.raise_pos_error()
        if value[0] < 0 or value[1] < 0:
            self.raise_pos_error()
        self.__position = value

    def my_print(self):
        """prints the circle to stdout with position offset"""
        print(self)

    def __str__(self) -> str:
        """string rep of the square"""
        if self.size == 0:
            return ""
        square = ""
        for _ in range(self.position[1]):
            square += "\n"
        for i in range(self.size):
            square += (" " * self.position[0])
            square += ("#" * self.size)
            if i != self.size - 1:
                square += "\n"
        return square
