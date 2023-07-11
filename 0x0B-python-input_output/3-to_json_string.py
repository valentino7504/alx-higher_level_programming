#!/usr/bin/python3
"""

This module returns the JSON representation of a string

"""


import json


def to_json_string(obj):
    """
    returns json rep of an object
    """
    return json.dumps(obj)
