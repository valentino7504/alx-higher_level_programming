#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    checked_list = []
    for num in my_list:
        if type(num) != int:
            checked_list.append(False)
        else:
            checked_list.append(num % 2 == 0)
    return checked_list
