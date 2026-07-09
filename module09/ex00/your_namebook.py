#!/usr/bin/env python3

def array_of_names(persons):
    names = []
    for first_name, last_name in persons.items():
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        names.append(full_name)
    return names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))

# Módulo é sobre dicionários (dict), equivalente a hash maps/objetos.

# .items() — método de dict que devolve pares (chave, valor). Aqui, unpacking direto no for: first_name, last_name recebem cada par automaticamente.
# .capitalize() — primeira letra maiúscula, resto minúsculo.
# .append() — adiciona item ao final de uma lista (mutação in-place, diferente de += em string).

# Sem novidade estrutural pra quem já conhece hash maps de outras linguagens — só a sintaxe do Python pra iterar (.items(), .keys(), .values()).
