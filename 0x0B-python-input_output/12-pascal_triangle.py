#!/usr/bin/python3
"""Function to print pascal's triangle"""


def pascal_triangle(n):
    """return a list of lists of integers representing\
        pascal's triangle"""
    trgle = []
    trgle.append([1])
    for i in range(n):
        new = []
        prev = trgle[-1]
        new.append(prev[0])
        for l in range(len(prev) - 1):
            new.append(prev[l] + prev[l + 1])
        new.append(prev[-1])
        trgle.append(new)
    return (trgle)
