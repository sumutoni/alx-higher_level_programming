#!/usr/bin/python3
"""Rectangle class inheriting from Base class"""
from  models.base import Base


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
        for li in range(self.__y):
            print()
        for i in range(self.__height):
            for s in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """assigns arguments to each attribute"""
        new_arg = [self.id, self.__width, self.__height, self.__x, self.__y]
        keys = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                new_arg[i] = args[i]
        else:
            for key in kwargs.keys():
                if key in keys:
                    new_arg[keys.index(key)] = kwargs[key]
        (self.id, self.__width, self.__height, self.__x, self.__y) = new_arg

    def __str__(self):
        """print rectangle to stdout"""
        str1 = ("[{}] ({:d}) {:d}/{:d} - {:d}".format
                (type(self).__name__, self.id, self.__x, self.__y,
                    self.__width, self.__height))
        if type(self).__name__ == 'Rectangle':
            str1 = str1 + "/{:d}".format(self.__height)
        return str1

    def to_dictionary(self):
        new_dict = {'id': self.id, 'width': self.__width,
                    'height': self.__height, 'x': self.__x,
                    'y': self.__y}
        return new_dict
