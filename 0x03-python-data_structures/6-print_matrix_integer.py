#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in len(row):
            if i != len(row) - 1:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
        print("")
