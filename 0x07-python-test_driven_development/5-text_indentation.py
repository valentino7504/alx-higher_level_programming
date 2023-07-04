#!/usr/bin/python3
"""
This is a module that prints a blank line
based on characters
It also has error checking and tests in the tests directory
"""


def text_indentation(text):
    """
    This implements the text indentation function as specified
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    prev = ""
    delimiters = [".", "?", ":"]
    for i in range(len(text)):
        space_flag = 0
        if text[i] == " " and (prev in delimiters or i == 0 or
                               prev == "\n"):
            continue
        elif text[i] == " ":
            looping = True
            j = i + 1
            while j < len(text) and looping:
                if text[j] == "\n":
                    i = j + 1
                    prev = text[j]
                    looping = False
                elif text[j].isalpha() or text[j] in delimiters:
                    print(text[i], end="")
                    looping = False
                j += 1
        elif text[i] in delimiters:
            print(text[i], end="")
            print("\n")
        else:
            print(text[i], end="")
        prev = text[i]
