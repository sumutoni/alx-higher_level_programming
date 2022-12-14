#!/usr/bin/python3
"""Square class inheriting from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class inheriting from Rectangle"""
    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area calculator"""
        return self.__size * self.__size

    def __str__(self):
        """prints square"""
        return ("[Square] {s}/{s}".format(s=self.__size))
