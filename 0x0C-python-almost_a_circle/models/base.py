#!/usr/bin/python3
"""The base class for other classes that will be created later"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """check if id is not None before assigning it value"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects