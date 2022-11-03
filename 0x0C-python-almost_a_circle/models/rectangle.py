#!/usr/bin/python3
"""Rectangle class inheriting from Base class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method"""
        return self.__width

    @property
    def height(self):
        """getter method"""
        return self.__height

    @property
    def x(self):
        """getter method"""
        return self.__x

    @property
    def y(self):
        """getter method"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter method"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter method"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter method"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calcluates area"""
        return self.__height * self.__width

    def display(self):
        """displays rectangle using # character"""
        for i in range(height):
            for j in range(width):
                print("#", end='')
            print()
