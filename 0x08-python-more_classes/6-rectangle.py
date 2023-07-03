#!/usr/bin/python3
"""

Definition of a rectangle class for use in
0x08 - more classes and objects

"""


class Rectangle:
    number_of_instances = 0
    """
    An rectangle class with width and height and
    methods to obtain the area and perimeter.
    This class also has a nice string representation to print it in
    the terminal/console and tracks the number of rectangle instances
    in the current environment.
    """
    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self) -> str:
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_string = ""
        for _ in range(self.height):
            rectangle_string += "#" * self.width
            rectangle_string += "\n"
        return rectangle_string.strip()

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self) -> None:
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
