#!/usr/bin/pyhton3
def add_integer(a, b=98):
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
