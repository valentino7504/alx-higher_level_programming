#!/usr/bin/python3
"""
creating a locked class in python
"""


class LockedClass:
    """
    My implementation of a locked class where you can only set
    first_name
    """
    __slots__ = ["first_name"]
