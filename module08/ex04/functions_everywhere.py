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


#             string[:8] — slice, pega os primeiros 8 caracteres ([start:end], omitindo start = começa do 0).
# while len(string) < 8: string += "Z" — loop comum, só concatenando até bater o tamanho. Nada específico de Python além da sintaxe (while cond: com indentação).
# Duas funções imprimindo direto (print dentro delas) em vez de retornar — funciona porque o enunciado só pede pra "mostrar", não reaproveitar o valor depois.
