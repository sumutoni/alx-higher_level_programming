#!/usr/bin/python3
"""A class Square with a private instance attribute size"""


class Square:
    """defining Square class and validating size value"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter Method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter Method"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A function to calculate area of square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
