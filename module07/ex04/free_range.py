#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    if a < b:
        values = list(range(a, b + 1))
        print(values)
    else:
        print("none")


# ## O que o enunciado pedia

# > - O programa recebe **2 números** como parâmetros.
# > - O primeiro número deve ser **estritamente menor** que o segundo.
# > - Construir um array com todos os valores **entre** esses dois números.
# > - Mostrar o array usando `print()`.
# > - Se o número de parâmetros for diferente de 2, mostrar `"none"`.
# > - Dica do PDF: *"Use the range function."*

# Exemplo do PDF:
# ```
# ?> ./free_range.py | cat -e
# none$
# ?> ./free_range.py 10 14 | cat -e
# [10, 11, 12, 13, 14]$
# ```

# ## `len(sys.argv) != 3`

# Mesma lógica de sempre: 2 parâmetros reais + nome do script = 3 itens em `sys.argv`.

# ## `int(sys.argv[1])` e `int(sys.argv[2])`

# Aqui está o primeiro ponto importante: **tudo que vem de `sys.argv` é string**, mesmo que pareça um número. Se você digitar `./free_range.py 10 14`, o Python recebe `"10"` e `"14"` (com aspas, como texto), não os números `10` e `14`.

# `int()` é uma função embutida de **conversão de tipo** (type casting): pega uma string que representa um número inteiro e converte para o tipo `int` de verdade. Sem essa conversão, eu não conseguiria comparar `a < b` numericamente (comparar strings usa ordem alfabética, não numérica — `"9" < "10"` seria `False`, porque "9" vem depois de "1" alfabeticamente!). Por isso a conversão é essencial aqui, não é só um detalhe estético.

# ## `if a < b:` — validação da regra "estritamente menor"

# O enunciado pede que o primeiro número seja **estritamente menor** que o segundo (não pode ser igual, tem que ser menor de verdade). Por isso o teste é `a < b`, não `a <= b`. Se a condição falhar (`a >= b`), cai no `else` e mostra `"none"` — isso cobre tanto o caso de `a` ser maior quanto de `a` ser igual a `b`.

# ## `range(a, b + 1)`

# Aqui está a dica do PDF em ação, e o detalhe mais importante do exercício: **`range()` não inclui o valor final por padrão**.

# `range(a, b)` gera os números de `a` até `b - 1` (parando **antes** de `b`). Mas o enunciado quer que `b` também apareça na lista final (veja o exemplo: `free_range.py 10 14` inclui o `14`). Por isso preciso escrever `range(a, b + 1)` — assim ele para em `b`, e não antes dele.

# Esse `+1` é um erro clássico (conhecido como **off-by-one error**, erro de "um a mais ou um a menos") que vale a pena saber explicar bem na avaliação: sem ele, `range(10, 14)` geraria `[10, 11, 12, 13]`, faltando o 14.

# ## `list(range(...))`

# `range()` sozinho não devolve uma lista pronta — ele devolve um **objeto range**, que é uma espécie de "gerador preguiçoso" de números (eficiente em memória, porque não guarda todos os números de uma vez, só sabe como gerá-los sob demanda). Para ter de fato uma lista visível e imprimível no formato `[10, 11, 12, 13, 14]`, preciso envolver com `list()`, que força a conversão, gerando todos os valores e guardando numa lista de verdade.

# ---

# **Resumo pra avaliação:** este exercício reúne três conceitos: **conversão de tipo com `int()`** (porque `sys.argv` sempre entrega strings, e comparação numérica exige números de verdade), a regra de que **`range(a, b)` exclui `b`** (por isso o `+1` para incluir o limite superior), e a diferença entre **`range()`** (objeto preguiçoso/gerador) e **`list()`** (força a materialização da sequência como uma lista concreta).
