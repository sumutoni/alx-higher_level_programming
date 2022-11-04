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
        return super().width

    @size.setter
    def size(self, value):
        """setter method"""
        Rectangle.width.fset(self, value)
        Rectangle.height.fset(self, value)

    def area(self):
        """calcluates area"""
        return super().area()

    def display(self):
        """displays square using # character"""
        super().display()

    def update(self, *args, **kwargs):
        """assigns arguments to each attribute"""
        super().update(args, kwargs)

    def __str__(self):
        """print square to stdout"""
        return super().__str__()
