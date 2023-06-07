#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if not matrix:
        return []
    n = len(matrix)
    for i in range(n):
        row = []
        for j in range(n):
            row.append(matrix[i][j] * matrix[i][j])
        new_matrix.append(row)
    return new_matrix
