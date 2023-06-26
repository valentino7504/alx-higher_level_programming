#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int(value)
    except ValueError:
        return False
    else:
        print("{:d}".format(int(value)))
        return True
