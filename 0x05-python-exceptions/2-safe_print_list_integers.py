#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed_numbers = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end = "")
        except (TypeError, ValueError):
            i += 1
            pass
        else:
            i += 1
            printed_numbers += 1
    print()
    return printed_numbers
