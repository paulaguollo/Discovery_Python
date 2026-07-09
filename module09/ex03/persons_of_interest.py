#!/usr/bin/env python3

def famous_births(figures):
    sorted_figures = sorted(figures.values(), key=lambda person: person["date_of_birth"])
    for person in sorted_figures:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)


# Dict aninhado: cada valor de figures é outro dict ({"name": ..., "date_of_birth": ...}).
# sorted(iterável, key=...) — ordena qualquer iterável; key recebe uma função que diz por qual campo ordenar (aqui, uma lambda que extrai date_of_birth de cada item). Não muda a lista original, retorna uma nova.
# Como as datas são strings de 4 dígitos ("1815", "1900"...), ordenação alfabética de string coincide com ordenação cronológica — só funciona por causa desse detalhe (mesmo número de dígitos).
# f-string: f"{var}" interpola variáveis direto na string, mesma ideia de template literals do JS (`${var}`) ou f-strings de outras linguagens.