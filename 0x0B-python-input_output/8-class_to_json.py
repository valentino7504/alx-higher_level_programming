#!/usr/bin/python3
'''

Returns the dictionary description of object

'''


import json


def class_to_json(obj):
    """
    returns dictionary json format of a class
    """
    return obj.__dict__
