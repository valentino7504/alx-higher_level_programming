#!/usr/bin/python3
"""Creates a circle class"""


import math


class Circle:
    """This is a circle class with radius, area and
    circumference"""
    def __init__(self, radius=0) -> None:
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """gets the area of the circle"""
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """gets the circumference of the circle"""
        return 2 * self.__radius * math.pi
