#!/usr/bin/python3
"""function that writes to file and returns written characters"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as fil:
        print(fil.write(text))
