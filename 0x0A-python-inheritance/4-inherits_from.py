#!/usr/bin/python3
"""

This module checks if an object is inherited from a class

"""


def inherits_from(obj, a_class):
    """
    This checks if obj inherits from a_class
    """
    return issubclass(type(obj), a_class) and a_class != type(obj)
