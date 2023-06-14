#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deleted_keys = [key for key in a_dictionary.keys()
                    if a_dictionary[key] == value]
    for key in deleted_keys:
        del a_dictionary[key]
    return a_dictionary
