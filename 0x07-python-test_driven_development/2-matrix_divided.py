#!/usr/bin/python3
"""
Matrix division module
Defines a function called matrix_divided
Checks for various errors
"""


def matrix_divided(matrix, div):
    """
    This function divides all the values in a matrix
    by a scalar
    Args:
    matrix - the matrix to be divided
    div - the number to divide the matrix by
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(matrix_error)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(matrix_error)
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(matrix_error)
    first_length = len(matrix[0])
    for row in matrix:
        if len(row) != first_length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda a: round(a/div, 2), row)))
    return new_matrix
