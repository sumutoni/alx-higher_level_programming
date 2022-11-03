#!/usr/bin/python3
"""Square class inheriting from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method"""
        return super().__width

    @size.setter
    def size(self, value):
        """setter method"""
        super().width(value)
        super().height(value)

    def area(self):
        """calcluates area"""
        return super().area()

    def display(self):
        """displays rectangle using # character"""
        super().display()

    def update(self, *args):
        """assigns arguments to each attribute"""
        (self.id, self.__width, self.__height, self.__x, self.__y) = args

    def __str__(self):
        """print rectangle to stdout"""
        str1 = ("[Square] ({:d}) {:d}/{:d} - {:d}".format
                (self.id, self.__x, self.__y,
                    self.__width))
        return str1
