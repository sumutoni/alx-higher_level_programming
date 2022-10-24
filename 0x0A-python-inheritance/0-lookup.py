#!/usr/bin/python3
"""get list of available attributes and methods of an object"""


def lookup(obj):
    """Returns list containing attributes and methods of obj"""
    return (dir(obj))
