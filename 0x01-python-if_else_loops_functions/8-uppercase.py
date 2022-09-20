#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        asc = ord(str[i])
        asc = asc - 32
        str = chr(asc) + str[(i + 1):]
    print("{}".format(str))
