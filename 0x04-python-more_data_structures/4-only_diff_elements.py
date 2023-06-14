#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_1 = set(filter(lambda x: x not in set_2, set_1))
    unique_2 = set(filter(lambda x: x not in set_1, set_2))
    return unique_1.union(unique_2)
