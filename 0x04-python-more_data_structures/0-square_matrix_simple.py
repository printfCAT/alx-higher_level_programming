#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    square_matrix = [[x ** 2 for x in row] for row in new_matrix]
    return square_matrix
