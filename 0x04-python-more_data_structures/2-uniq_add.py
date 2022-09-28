#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_l = list(set(my_list))
    result = 0
    for i in set_l:
        result += i
    return result
