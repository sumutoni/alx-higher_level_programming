#!/usr/bin/python3
"""append text to a file and return number of appended characters"""


def append_write(filename="", text=""):
    """append text to file and return number of appended characters"""
    with open(filename, "a", encoding="utf-8") as fil:
        char = fil.write(text)
    return char
