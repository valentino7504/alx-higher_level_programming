#!/usr/bin/python3
"""
This module defines a function to print
a square in the console.
Also has error checking.
"""


def print_square(size):
    """
    A function that prints a square of side size with #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
