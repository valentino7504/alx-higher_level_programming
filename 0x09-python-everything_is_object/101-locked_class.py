#!/usr/bin/python3
"""
creating a locked class in python
"""


class LockedClass:
    """
    My implementation of a locked class where you can only set
    first_name
    """

    def __init__(self) -> None:
        pass

    def __setattr__(self, __name: str, __value) -> None:
        error_msg = f"'LockedClass' object has no attribute '{__name}'"
        if not hasattr(self, "first_name") and __name == "first_name":
            super().__setattr__("first_name", __value)
        else:
            raise AttributeError(error_msg)
