#!/usr/bin/python3
"""A class Square with a private instance attribute size"""


class Square:
    """defining Square class and validating size value"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """A function to calculate area of square"""
        return self.__size ** 2
