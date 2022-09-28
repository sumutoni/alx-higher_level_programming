#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    new = [replace if i == search else i for i in new]
    return new
