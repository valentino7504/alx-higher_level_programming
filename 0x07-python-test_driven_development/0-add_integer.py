#!/usr/bin/python3
"""
This module contains a function for integer addition
It handles improper input properly.
Tests for the function are found in the tests directory
"""


def add_integer(a, b=98):
    """
    Addition function: add_integer(3, 4) -> 7
    """
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
