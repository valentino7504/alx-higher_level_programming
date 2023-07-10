#!/usr/bin/python3
"""

adds a new attribute to an object if possible

"""


def add_attribute(obj, name, value):
    """
    this is the function that actually adds attributes to object
    if and when possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
