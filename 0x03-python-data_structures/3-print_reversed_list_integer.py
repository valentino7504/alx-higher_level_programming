#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    for num in range(length):
        print("{:d}".format(my_list[length - num - 1]))
