#!/usr/bin/python3
"""

Definition of a rectangle class for use in
0x08 - more classes and objects

"""


class Rectangle:
    """
    An rectangle class with width and height and
    methods to obtain the area and perimeter.
    This class also has a nice string representation to print it in
    the terminal/console and tracks the number of rectangle instances
    in the current environment.
    It can also check which rectangle has a larger area and create square-like
    instances.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

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
            rectangle_string += str(self.print_symbol) * self.width
            rectangle_string += "\n"
        return rectangle_string.strip()

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self) -> None:
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
