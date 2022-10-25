#!/usr/bin/pytho
"""Create object from JSON file"""
import json


def load_from_json_file(filename):
    """create object from JSON file"""
    with open(filename, "r", encoding="utf-8") as fil:
        line = fil.readline()
    obj = json.load(line)
