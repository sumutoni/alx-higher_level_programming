#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_l = []
    new_l = [my_list[i] for i in range(len(my_list)) if i != idx]
    del my_list[idx]
    return new_l
