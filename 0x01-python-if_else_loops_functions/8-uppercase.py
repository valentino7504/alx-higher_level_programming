#!/usr/bin/python3
def uppercase(old_string):
    new_string = ""
    for letter in old_string:
        if 97 <= ord(letter) <= 122:
            new_string += chr(ord(letter) - 32)
        else:
            new_string += letter
    print("{}".format(new_string))
    return new_string
