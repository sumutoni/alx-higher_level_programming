#!/usr/bin/python3
import sys
if __name__ = "__main__":
    lg = len(argv[1:])
    if lg == 0:
        print("{:d} arguments.".format(lg))
    else:
        if lg == 1:
            print("{:d} argument:".format(lg))
            print("1: {}".format(argv[1]))
        else:
            print("{:d} arguments:".format(lg))
            for i in range (1, (lg + 1)):
                print("{:d}: {}".format(i, argv[i]))
