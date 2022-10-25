#!/usr/bin/python3
"""defining class Student with instance attributes\
    first_name, last_name, and age"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary description of object"""
        return (self.__dict__.copy())
