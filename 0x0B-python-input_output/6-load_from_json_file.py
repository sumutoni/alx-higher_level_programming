#!/usr/bin/python3
"""Create object from JSON file"""
import json


def load_from_json_file(filename):
    """create object from JSON file"""
    with open(filename, "r", encoding="utf-8") as fil:
        obj = json.load(fil)
    return obj
