#!/usr/bin/python3
"""Function to add arguments to python list and saving them in json file"""
import sys
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file


def add_item(args=[]):
    """adds arguments to list and saves them to JSON file"""
    try:
        fil = "add_item.json"
        elements = load(fil)
    except FileNotFoundError:
        elements = []
    new_list = elements + args
    save(new_list, fil)


if __name__ == "__main__":
    add_item(sys.argv[1:])
