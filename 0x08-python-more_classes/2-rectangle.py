#!/usr/bin/python3

""" An empty class Rectangle """


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """ initialization method(constructor)"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            """setter method for width"""
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter method for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to calculate area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """method to calculate perimeter, is 0 if height or width is 0"""
        if self.height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))
