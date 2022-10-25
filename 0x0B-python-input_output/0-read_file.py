#!/usr/bin/python3
""" function that reads file and prints its content"""


def read_file(filename=""):
    """reads from file and prints content to stdout"""
    with open(filename, "r", encoding="utf-8") as fil:
        print(fil.read(), end="")
