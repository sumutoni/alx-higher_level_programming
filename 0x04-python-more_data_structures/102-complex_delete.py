#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    key = [k for k in a_dictionary.keys() if a_dictionary[k] == value]
    for i in key:
        del a_dictionary[i]
    return a_dictionary
