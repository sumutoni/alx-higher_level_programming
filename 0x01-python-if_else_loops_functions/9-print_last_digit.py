#!/usr/bin/python3
def print_last_digit(number):
    last = -1 * number % 10
    print(f"{last:d}", end="")
    return last
