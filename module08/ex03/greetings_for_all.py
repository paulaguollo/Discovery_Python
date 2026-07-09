#!/usr/bin/env python3

def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print("Hello, " + name + ".")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)

# Parâmetro default: name="noble stranger" — se você chamar greetings() sem argumento, ele usa esse valor automaticamente. Igual a default parameters em C++/JS, mesma ideia.
# isinstance(name, str): checagem de tipo em runtime. Como Python não tem tipagem estática, isso é o jeito idiomático de perguntar "esse valor é uma string?". Retorna True/False. Aqui é usado pra pegar o caso greetings(42) — 42 é int, não str, então cai no erro.

# Repara que o programa não recebe argumentos via terminal — as chamadas (greetings('Alexandra'), etc.) já estão hardcoded no próprio arquivo.
