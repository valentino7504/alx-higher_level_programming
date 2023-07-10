#!/usr/bin/python3
"""

This module is a class that inherits from the python list class

"""


class MyList(list):
    """
    A list that inherits from Python's own list class
    """
    def __init_subclass__(cls) -> None:
        super().__init__()

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
