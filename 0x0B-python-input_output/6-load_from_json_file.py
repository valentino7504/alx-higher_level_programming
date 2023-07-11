#!/usr/bin/python3
'''

This module loads a json string as an object from a file

'''


import json


def load_from_json_file(filename):
    """
    reads a file and obtains a json object from it
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
