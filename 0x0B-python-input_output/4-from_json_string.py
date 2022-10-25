#!/usr/bin/python3
"""convert JSON string to pythoon data structure"""
import json


def from_json_string(my_str):
    """converts JSON string to python data structure"""
    my_obj = json.loads(my_str)
    return my_obj
