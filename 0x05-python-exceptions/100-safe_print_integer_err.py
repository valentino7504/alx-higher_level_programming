#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(e))
        return False
    else:
        return True
