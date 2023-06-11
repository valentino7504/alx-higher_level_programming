#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if type(my_list) != list:
        return
    my_list.reverse()
    for num in my_list:
        print("{:d}".format(num))
