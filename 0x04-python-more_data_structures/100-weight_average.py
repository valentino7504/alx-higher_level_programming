#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(list) == 0:
        return 0
    denominator = 0
    weighted_sum = 0
    for score in my_list:
        weighted_sum += score[0] * score[1]
        denominator += score[1]
    return weighted_sum/denominator
