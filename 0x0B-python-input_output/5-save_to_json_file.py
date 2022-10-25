#!/usr/bin/python3
"""converts object to JSON and saves to file"""
import json


def save_to_json_file(my_obj, filename):
    """converts object to JSON and save to file"""
    with open(filename, "w", encoding="utf-8") as fil:
        json.dump(my_obj, fil)
