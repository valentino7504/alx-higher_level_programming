#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print(my_list[i], end="")
        except IndexError:
            i -= 1
            break
    print()
    return i + 1
