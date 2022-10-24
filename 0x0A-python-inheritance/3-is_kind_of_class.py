#!/usr/bin/python3
""" checks if object is instance of specified class of its children"""
def is_kind_of_class(obj, a_class):
    """return true if obj is of instance a_class or of its children"""
    return isinstance(obj, a_class)
