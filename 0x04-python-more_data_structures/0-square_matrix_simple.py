#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    mat = [[i**2 for i in row] for row in matrix]
    return mat
