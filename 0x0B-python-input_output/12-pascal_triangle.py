#!/usr/bin/python3
'''

This is a module that generates a pascal triangle

'''


def pascal_triangle(n):
    """
    this generates a pascal triangle of n rows
    """
    row = []
    if n <= 0:
        return []
    triangle = pascal_triangle(n - 1)
    for i in range(n):
        if i == 0 or i == n - 1:
            row.append(1)
        else:
            row.append(triangle[-1][i] + triangle[-1][i - 1])
    triangle.append(row)
    return triangle
