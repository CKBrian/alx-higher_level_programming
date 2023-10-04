#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ divides all elements of a matrix """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for ls in matrix:
        if len(ls) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(x / div, 2) for x in lists] for lists in matrix]
    return new_matrix
