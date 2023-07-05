#!/usr/bin/python3
"""
say_my_name
This is a module which defines the function
called say_my_name which has different error handling
scenarios.
"""


def say_my_name(first_name, last_name=""):
    """
    Functions that prints first_name + last_name with error checking
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
    return
