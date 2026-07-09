#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) < 2:
    print("none")
else:
    for word in reversed(args):
        print(word)

# slicing** (`sys.argv[1:]`) para isolar os parâmetros reais 
#reversed() para percorrer uma lista de trás pra frente sem alterar a lista original. "só percorrer ao contrário".
