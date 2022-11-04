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
        new_arg = [self.id, self.__size, self.__size, self.__x, self.__y]
        if args is not None and len(args) > 0:
            for i, j in range(len(args)):
                if i == 1:
                    new_arg[j] = args[i]
                    j += 1
                new_args[j] = args[i]
            super().update(new_arg, kwargs)
        else:
            if 'size' in kwargs.keys():
                dict = {'width': kwargs['size'], 'height': kwargs['size']}
                kwargs.update(dict)
                super().update(args, kwargs)

    def __str__(self):
        """print square to stdout"""
        return super().__str__()
