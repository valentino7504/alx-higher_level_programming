#!/usr/bin/python3
"""Creates a square class with private size"""


class Square:
    """A square class with a private size"""
    def __init__(self, size) -> None:
        self.__size = size
