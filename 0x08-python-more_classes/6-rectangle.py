#!/usr/bin/python3

""" An empty class Rectangle """


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initialization method(constructor)"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """returns string representantion of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for j in range(self.__height)])

    def __repr__(self):
        """returns a representation of the rectangle class"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """prints message when instance is destroyed"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
