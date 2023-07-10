#!/usr/bin/python3
"""

This module checks if an object is an instance of a class
or is inherited from it

"""


def is_kind_of_class(obj, a_class):
    """
    This checks if obj is an instance of a_class or inherits
    """
    return isinstance(obj, a_class)
