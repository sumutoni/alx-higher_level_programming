#!/usr/bin/python3
"""function that writes to file and returns written characters"""


def write_file(filename="", text=""):
    """ write to file and return characters written"""
    with open(filename, "w", encoding="utf-8") as fil:
        characters = fil.write(text)
    return characters
