#!/usr/bin/python3
# 3-infinite_add.py
# A script that prints the result of the addition of all arguments.

import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # exclude script name
    total = 0

    for arg in args:
        total += int(arg)  # cast argument to int and add to total

    print(total)
