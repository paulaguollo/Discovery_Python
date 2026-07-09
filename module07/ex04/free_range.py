#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    if a < b:
        values = list(range(a, b + 1))
        print(values)
    else:
        print("none")
