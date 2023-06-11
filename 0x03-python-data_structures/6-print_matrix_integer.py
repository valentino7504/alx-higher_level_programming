#!/usr/bin/python3
def print_matrix_integer(matrix = [[]]):
    if matrix == [[]]:
        print()
        return
    for row in matrix:
        for i in range(len(row)):
            end = " " if i != len(row) - 1 else "\n"
            print("{}".format(row[i]), end=end)
