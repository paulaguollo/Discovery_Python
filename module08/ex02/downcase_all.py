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


# Junta o que já vimos: função com return + .lower() aplicada em loop sobre sys.argv[1:].
# Nada novo de Python aqui — só combinação de conceitos anteriores (função definida no módulo 8, sys.argv do módulo 6/7).
