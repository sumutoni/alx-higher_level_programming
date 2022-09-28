#!/usr/bin/python3
def subtract(a, b):
    return a - b


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if len(roman_string) == 1:
        result = sym.get(roman_string[0])
        return result
    sub = False
    for i in range(0, (len(roman_string) - 1)):
        if sym.get(roman_string[i]) >= sym.get(roman_string[i + 1]):
            if (not sub or sub) and i == len(roman_string) - 2:
                result += sym.get(roman_string[i + 1])
            if sub:
                sub = False
                pass
            result += sym.get(roman_string[i])
        else:
            result += subtract(sym.get(roman_string[i + 1]),
                               sym.get(roman_string[i]))
            sub = True
    return result
