#!/usr/bin/python3
"""

This module defines a function that reads a text file

"""


def read_file(filename=""):
    """
    reads the contents of a text file
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
