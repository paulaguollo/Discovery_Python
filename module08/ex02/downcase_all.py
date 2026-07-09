#!/usr/bin/env python3
import sys

def downcase_it(string):
    return string.lower()

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for word in args:
        print(downcase_it(word))
