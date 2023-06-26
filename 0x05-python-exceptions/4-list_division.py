#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    i = 0
    while i < list_length:
        division_result = 0
        try:
            division_result = my_list_1[i]/my_list_2[i]
        except IndexError:
            division_result = 0
            print("out of range")
        except (ValueError, TypeError):
            division_result = 0
            print("wrong type")
        except ZeroDivisionError:
            division_result = 0
            print("division by 0")
        finally:
            i += 1
            result_list.append(division_result)
    return result_list
