#!/usr/bin/python3
"""

This module writes to a file

"""


def write_file(filename="", text=""):
    """
    This function writes content to a file
    """
    with open(filename, "w", encoding="utf-8") as file:
        written = file.write(text)
    return written
