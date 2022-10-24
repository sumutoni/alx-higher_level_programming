#!/usr/bin/python3
"""Rectangle class inheriting from BaseGeometry"""


class Rectangle(7-base_geometry.BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """constructor"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
