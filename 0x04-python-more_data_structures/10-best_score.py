#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    great = 0
    for k in a_dictionary.keys():
        if a_dictionary[k] > great:
            great = a_dictionary[k]
            key = k
    return key
