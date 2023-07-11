#!/usr/bin/python3
"""

This module returns the Python object of a JSON string

"""


import json


def from_json_string(my_str):
    """
    returns python rep of json strings
    """
    return json.loads(my_str)
