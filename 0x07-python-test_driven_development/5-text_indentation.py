#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    for ch in range(len(text)):
        if text[ch] == '.' or text[ch] == '?' or text[ch] == ':':
            print(text[ch], end="")
            print()
            print()
        if text[ch] == ' ' and (prev == '?' or prev == '.' or prev == ':'):
                continue
        else:
            print(text[ch], end="")
        prev = text[ch]
