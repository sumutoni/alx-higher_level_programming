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

    def to_json(self, attrs=None):
        """return dictionary description of object"""
        copy = self.__dict__.copy()
        new_dict = {}
        if type(attrs) == list:
            for i in attrs:
                if type(i) != str:
                    return copy
            for item in attrs:
                for obj in copy:
                    if item == copy:
                        new_dict[obj] = copy[obj]
            return new_dict
        return copy

    def reload_from_json(self, json):
        """replaces all attaributes of instance"""
        for obj in json:
            self.__dict__[obj] = json[obj]

