#!/usr/bin/python3
"""Rectangle class inheriting from Base class"""
Base = __import__('base').Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super(id)
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
        if value <= 0:
            raise ValueError("Width must be > 0")
        if type(value) != int:
            raise TypeError("Width must be an integer")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter method"""
        if value <= 0:
            raise ValueError("Height must be greater than 0")
        if type(value) != int:
            raise TypeError("Height must be an integer")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter method"""
        if value < 0:
            raise ValueError("X must be greater than or equal to 0")
        if type(value) != int:
            raise TypeError("X must be an integer")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter method"""
        if value < 0:
            raise ValueError("Y must be greater than or equal to 0")
        if type(value) != int:
            raise TypeError("Y must be an integer")
        self.__y = value
