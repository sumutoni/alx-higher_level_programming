#!/usr/bin/python3
"""Made additions to BaseGeomtry class"""


class BaseGeometry():
    """Improved class"""

    def __init__(self):
        """initialization method"""
        pass

    def area(self):
        """calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
