#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    print("parameters: " + str(len(args)))
    for word in args:
        print(word + ": " + str(len(word)))



# ## O que o enunciado pedia

# > - Mostrar `"parameters:"` seguido do total de parâmetros passados.
# > - Para cada parâmetro, mostrar ele mesmo e seu tamanho.
# > - Se não houver parâmetros, mostrar `"none"`.
# > - **Regra especial:** deve usar um `for`, não um `while`.

# Exemplo do PDF:
# ```
# ?> ./count_it.py | cat -e
# none$
# ?> ./count_it.py "Game" "of" "Thrones" | cat -e
# parameters: 3$
# Game: 4$
# of: 2$
# Thrones: 7$
# ```

# ## `args = sys.argv[1:]`

# Mesmo truque do `aff_rev_params.py`: slicing para isolar só os parâmetros reais, sem o nome do script. Deixa o resto do código mais limpo — trabalhamos só com `args` daqui pra frente.

# ## `len(args) == 0`

# Aqui a checagem é mais simples que nos exercícios anteriores: só precisamos saber se **não veio nenhum** parâmetro (lista vazia), não importa se veio 1, 2 ou 100 — todos são aceitos.

# ## `str(len(args))`

# Aqui aparece um detalhe técnico importante: **concatenação de strings com `+`**. Em Python, você só pode usar `+` entre dois valores do **mesmo tipo** — não dá pra somar uma string com um número diretamente. `len(args)` devolve um **inteiro** (`int`), então preciso converter esse número para string com `str()` antes de conseguir "colar" (`+`) com o texto `"parameters: "`.

# Se eu tentasse `"parameters: " + len(args)` sem o `str()`, o Python daria erro (`TypeError: can only concatenate str (not "int") to str`).

# ## `for word in args:`

# Aqui está a exigência do enunciado: usar `for` em vez de `while`. O `for` percorre diretamente os **itens** da lista `args` (não índices) — a cada volta do laço, `word` recebe o próximo elemento da lista automaticamente, sem precisar controlar manualmente um contador (`i = 0`, `i += 1`, etc.) como seria necessário num `while`.

# Isso é uma diferença conceitual boa pra saber explicar: **`for` em Python é feito pra iterar sobre coleções** (listas, strings, dicionários...) de forma direta; já um `while` exigiria você mesmo gerenciar o índice e a condição de parada, tornando o código mais verboso e mais sujeito a erros (como esquecer de incrementar o índice e criar um loop infinito).

# ## `print(word + ": " + str(len(word)))`

# Mesma lógica de concatenação: `word` já é string, `": "` é string, mas `len(word)` (tamanho da palavra) é `int` — de novo precisa de `str()` para poder juntar tudo com `+`.

# ---

# **Resumo pra avaliação:** este exercício reforça `sys.argv[1:]` e reforça que **`+` entre strings e números não funciona sem conversão explícita** (`str()`), além de exigir explicitamente o uso de `for` — que em Python itera diretamente sobre os elementos de uma lista, sem precisar de um contador manual como no `while`.
