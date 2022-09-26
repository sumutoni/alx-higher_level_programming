#!/usr/bin/python3
def append_0(tup=()):
    tup_l = list(tup)
    if len(tup) == 0:
        tup_l.append(0)
        tup_l.append(0)
        tup = tuple(tup_l)
    if len(tup) == 1:
        tup_l.append(0)
        tup = tuple(tup_l)
    return tup


def add_tuple(tuple_a=(), tuple_b=()):
    tup = []
    tup_t = ()
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        tup.append(0)
        tup.append(0)
        tup_t = tuple(tup)
    else:
        tuple_a = append_0(tuple_a)
        tuple_b = append_0(tuple_b)
        for i in range(2):
            tup.append(tuple_a[i] + tuple_b[i])
        tup_t = tuple(tup)
    return tup_t
