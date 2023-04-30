#!/usr/bin/python3
""" define a function """


def matrix_divided(matrix, div):
    """
        Args:
            matrix (list). list of lists
            div (int/float). number to be the divisor
    """
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    divided_matrix = []
    for row in matrix:
        divided_row = []
        for elem in row:
            divided_row.append(round(elem / div, 2))
        divided_matrix.append(divided_row)
    return divided_matrix
