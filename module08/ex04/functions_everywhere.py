#!/usr/bin/env python3
import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    while len(string) < 8:
        string += "Z"
    print(string)

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for word in args:
        if len(word) > 8:
            shrink(word)
        elif len(word) < 8:
            enlarge(word)
        else:
            print(word)
