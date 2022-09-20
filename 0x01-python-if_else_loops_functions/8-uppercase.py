#!/usr/bin/python3
def uppercase(str):
    strU = ""
    for i in range(0, len(str)):
        asc = ord(str[i])
        if asc >= 65 and asc <= 90:
            strU = strU + str[i]
        elif asc >= 97 and asc <= 122:
            asc = asc - 32
            strU = strU + chr(asc)
        else:
            strU = strU + str[i]
    print("{}".format(strU))
