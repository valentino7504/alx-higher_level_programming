#!/usr/bin/python
"""
creating a locked class in python
"""


class LockedClass:
    """
    a class where you can only create attribute first_name
    """
    __slots__ = ["first_name"]
