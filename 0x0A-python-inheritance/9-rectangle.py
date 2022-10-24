#!/usr/bin/python3
"""Rectangle class inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """constructor"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """implementing area"""
        return self.__width * self.__height

    def __str__(self):
        """prints rectangle"""
        return ("[Rectangle] {w}/{h}".format(w=self.__width, h=self.__height))
