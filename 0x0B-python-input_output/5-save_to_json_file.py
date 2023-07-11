#!/usr/bin/python3
'''

This file is used to save json format of an object to a file


'''


import json


def save_to_json_file(my_obj, filename):
    """
    saves the json string to a file
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
