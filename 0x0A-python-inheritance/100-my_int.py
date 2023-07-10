#!/usr/bin/python3
"""

MyInt class that inherits from the default int class

"""


class MyInt(int):
    """
    MyInt inherits from the default int class with some changes
    """
    def __init__(self, value) -> None:
        self.__int__ = value
        super().__init__()

    def __eq__(self, __value: object) -> bool:
        return self.__int__ == __value.__int__

    def __ne__(self, __value: object) -> bool:
        return self.__int__ != __value.__int__
