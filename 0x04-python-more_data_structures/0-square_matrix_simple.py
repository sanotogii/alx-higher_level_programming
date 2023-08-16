#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for item in matrix:
        row = []
        for i in item:
            row.append(i ** 2)
        new_matrix.append(row)
    return (new_matrix)
