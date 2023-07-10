#!/usr/bin/python3
"""
A module to return the list of attributes and
methods of an object
"""


def lookup(obj):
    """
    This function returns all attributes and methods
    of obj
    """
    return dir(obj)
