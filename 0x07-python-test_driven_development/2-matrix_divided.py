#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    size = len(matrix[0])
    for list in matrix:
        if size != len(list):
            raise TypeError("each row of the matrix must have the same size")
    for list in matrix:
        for i in list:
            if type(i) != float and type(i) != int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_l=[]
    j = 0
    for list in matrix:
        new_l.append([])
        for i in list:
            new_l[j].append(round(i / div, 2))
        j += 1
    return new_l
