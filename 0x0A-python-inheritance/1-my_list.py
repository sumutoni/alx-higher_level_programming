#!/usr/bin/python3
"""A class that inherits from list"""


class MyList(list):
    """Class inheriting from list"""

    def __init__(self):
        """initialization method"""
        pass

    def print_sorted(self):
        """prints element of list in sorted order"""
        print(sorted(self))
