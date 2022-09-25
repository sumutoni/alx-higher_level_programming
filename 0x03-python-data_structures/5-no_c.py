#!/usr/bin/python3
def no_c(my_string):
    letters = [c for c in my_string if (c.upper() != 'C')]
    return ("".join(letters))
