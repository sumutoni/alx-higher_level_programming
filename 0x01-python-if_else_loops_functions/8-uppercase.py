#!/usr/bin/python3
def uppercase(str):
    strU = ""
    for i in range(0, len(str)):
        asc = ord(str[i])
        asc = asc - 32
        strU = strU + chr(asc)
    print("{}".format(strU))
