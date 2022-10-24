#!/usr/bin/python3
"""checks if object is instance of subclass of a specified class"""


def inherits_from(obj, a_class):
    """returns true if obj is instance of subclass of a_class but not
            instance of a_class"""
    return (issubclass(obj, class) and (type(obj) is not a_class))
