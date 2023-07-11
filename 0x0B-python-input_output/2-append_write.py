#!/usr/bin/python3
"""

This mmodule appends text to a file

"""


def append_write(filename="", text=""):
    """
    This function appends text to a file named filename
    """
    with open(filename, "a", encoding="utf-8") as file:
        written = file.write(text)
    return written
