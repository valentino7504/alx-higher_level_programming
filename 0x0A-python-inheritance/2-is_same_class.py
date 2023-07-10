#!/usr/bin/python3
"""

This module checks if an object is an instance of a class

"""


def is_same_class(obj, a_class):
    """
    This checks if obj is an instance of a_class
    """
    return type(obj) == a_class
