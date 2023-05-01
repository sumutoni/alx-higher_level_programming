#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if list_of_integers:
        list_of_integers = sorted(list_of_integers)
        return(list_of_integers[-1])
    else:
        return None
