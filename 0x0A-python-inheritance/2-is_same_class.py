#!/usr/bin/python3
""" check if object if of specified class"""


def is_same_class(obj, a_class):
    """returns true if obj is instance of a_class"""
    return type(obj) == a_class
