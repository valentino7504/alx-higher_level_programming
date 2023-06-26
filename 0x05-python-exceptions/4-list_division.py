#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = [0] * list_length
    i = 0
    while i < list_length:
        try:
            result_list[i] = my_list_1[i]/my_list_2[i]
        except IndexError:
            print("out of range")
            return result_list
        except (ValueError, TypeError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        i += 1
    return result_list
