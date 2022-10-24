#!/usr/bin/python3
"""Square class inheriting from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class inheriting from Rectangle"""
    def __init__(self, size):
        """constructor"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """area calculator"""
        return self.__size * self.__size
