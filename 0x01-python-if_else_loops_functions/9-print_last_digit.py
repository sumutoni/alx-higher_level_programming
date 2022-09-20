#!/usr/bin/python3
def print_last_digit(number):
    last = 0
    if number < 0:
        last = -1 * number % 10
        print(f"{last:d}", end="")
    else:
        last = number % 10
        print(f"{last:d}", end="")
    return last
