#!/usr/bin/python3
def print_square(size):
    """prints square using # character"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
