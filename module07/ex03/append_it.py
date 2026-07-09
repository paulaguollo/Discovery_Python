#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for word in args:
        if word.endswith("ism"):
            continue
        print(word + "ism")
