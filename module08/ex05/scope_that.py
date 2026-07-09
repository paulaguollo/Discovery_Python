#!/usr/bin/env python3

def add_one(number):
    number = number + 1
    return number

my_var = 5
print(my_var)
add_one(my_var)
print(my_var)

# Observation:
# The value of my_var does not change after calling add_one(my_var).
# In Python, when we pass an integer to a function, only its value is
# copied into the function's local parameter ("number"). Modifying
# "number" inside add_one only affects that local variable, which
# exists in the function's own scope. Once the function returns, that
# local scope disappears and my_var in the main program is untouched.


# Saída: 5 depois 5 de novo (não vira 6). Esse é o conceito central do exercício — escopo de função.

# number é um parâmetro local: quando chamo add_one(my_var), o valor de my_var (5) é copiado para number. int é imutável em Python, então number = number + 1 cria um número novo e reatribui number — isso não afeta my_var de forma alguma.
# Isso é equivalente a pass by value (como em C para tipos primitivos). Diferente de listas/dicts, que são mutáveis e, se você alterasse o conteúdo in place (ex: lista.append(x)), isso sim afetaria o objeto original, porque aí você estaria mexendo no mesmo objeto na memória, não criando um novo.
# Pra my_var realmente mudar, precisaria de my_var = add_one(my_var) (reatribuir o retorno) ou usar global dentro da função (geralmente evitado, má prática).
