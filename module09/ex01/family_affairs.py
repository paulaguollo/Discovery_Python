#!/usr/bin/env python3

def find_the_redheads(family):
    redheads = filter(lambda first_name: family[first_name] == "red", family.keys())
    return list(redheads)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))


# lambda — função anônima de uma linha só. lambda x: expressão é equivalente a uma arrow function (x => expressão em JS). Aqui: lambda first_name: family[first_name] == "red".
# filter(função, iterável) — programação funcional: aplica a função a cada item de family.keys() e mantém só os que retornam True.
# filter() sozinho não devolve lista — devolve um objeto lazy (avaliação preguiçosa, só gera valores quando pedido). Por isso o list() no final, pra materializar.