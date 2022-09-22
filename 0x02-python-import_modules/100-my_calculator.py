#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    lt = len(sys.argv)
    if lt != 4:
        print("./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = {"+": add(a, b), "-": sub(a, b),  "*": mul(a, b), "/": div(a, b)}
    if sys.argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        result = int(op[sys.argv[2]])
        print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, result))
