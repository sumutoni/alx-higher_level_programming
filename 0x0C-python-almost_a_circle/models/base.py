#!/usr/bin/python3
"""The base class for other classes that will be created later"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of list_objs to file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as fil:
            if list_objs is None:
                json.dump([], fil)
            else:
                list_dict = []
                for item in list_objs:
                    list_dict.append(item.to_dictionary())
                json_str = cls.to_json_string(list_dict)
                fil.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns list representation of json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set"""
        instance = None
        li = []
        if cls.__name__ == 'Rectangle':
            instance = cls(2, 2)
        else:
            instance = cls(2)
        instance.update(*li, **dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as fil:
                json_str = fil.read()
                json_list = cls.form_json_string(json_str)
                instances = []
                for item in json_list:
                    instances.append(cls.create(**item))
                return instances
        except:
            return []
