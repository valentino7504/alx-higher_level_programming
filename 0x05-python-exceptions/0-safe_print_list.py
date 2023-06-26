#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            my_list[i]
        except (IndexError, TypeError):
            print()
            return i
        else:
            print(my_list[i], end="")
    print()
    return i + 1
