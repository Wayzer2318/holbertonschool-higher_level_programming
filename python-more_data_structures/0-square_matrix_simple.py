#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        nrow = [j * j for j in i]
        new_matrix.append(nrow)
    return new_matrix
