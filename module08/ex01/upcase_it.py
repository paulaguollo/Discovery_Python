#!/usr/bin/env python3

def upcase_it(string):
    return string.upper()

print(upcase_it("hello"))

# Parâmetro sem tipo declarado (string, não str string) — Python é dynamically typed, o tipo só existe em runtime.
# return funciona como em qualquer linguagem: devolve o valor e sai da função.
# .upper() é método de string, retorna string nova (strings são imutáveis, tipo Java/JS, não como um char[] mutável de C).
