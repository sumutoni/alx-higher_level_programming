#!/usr/bin/pyhton3
def add_integer(a, b=98):
    if not (isinstance(a, int) and isinstance(a, float)):
        raise TypeError("a must be  an integer")
    if not (isinstance(b, int) and isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
