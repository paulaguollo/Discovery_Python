#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for word in args:
        if word.endswith("ism"):
            continue
        print(word + "ism")

# ## O que o enunciado pedia

# > - Mostrar cada parâmetro, um por um, **acrescentando** "ism" no final.
# > - Se um parâmetro **já terminar** com "ism", ele deve ser **pulado** (não mostrado).
# > - Se não houver parâmetros, mostrar `"none"`.
# > - Dica do PDF: *"Use find."*

# Exemplo do PDF:
# ```
# ?> ./append_it.py "parallel" "egoism" "human" | cat -e
# parallelism$
# humanism$
# ```

# Repare: "egoism" **desaparece** do output — ele já termina em "ism", então é ignorado por completo (nem "egoismism" nem "egoism" aparecem).

# ## `word.endswith("ism")`

# Aqui está o conceito novo: `.endswith()` é um **método de string** que verifica se ela **termina** com um determinado sufixo, devolvendo `True` ou `False`. É exatamente pra isso que existe — evita você ter que fazer manualmente algo como comparar os últimos 3 caracteres com fatiamento (`word[-3:] == "ism"`), embora isso também funcionasse.

# A dica do PDF (*"Use find"*) se refere ao método `.find()`, que é uma abordagem alternativa: ele procura uma substring dentro de outra e devolve a **posição** onde ela começa (ou `-1` se não encontrar). Daria pra resolver assim também, verificando se `word.find("ism") == len(word) - 3`, mas `.endswith()` é mais direto e expressa melhor a intenção do código — por isso escolhi ele. Se te perguntarem na avaliação, você pode mencionar as duas formas e explicar por que preferiu uma.

# ## `continue`

# Esse é o outro conceito novo. Dentro de um loop (`for` ou `while`), `continue` **interrompe a iteração atual imediatamente** e pula direto para a próxima volta do laço — sem executar o resto do código que vem depois dele naquela iteração.

# Aqui, quando `word.endswith("ism")` é `True`, o `continue` faz o programa **pular o `print()`** que viria a seguir e ir direto pra próxima palavra da lista. É assim que "egoism" nunca chega a ser impresso.

# Alternativa sem `continue`, só pra comparar (mesmo resultado):
# ```python
# for word in args:
#     if not word.endswith("ism"):
#         print(word + "ism")
# ```
# Ambas funcionam — `continue` é útil quando você quer "descartar casos indesejados logo no início do loop" e manter o resto do código (o `print`) sem precisar aninhar num `if` adicional. É uma questão de estilo/legibilidade.

# ## `print(word + "ism")`

# Concatenação simples de strings — junta a palavra original com o sufixo "ism" (ex: "parallel" + "ism" = "parallelism").

# ---

# **Resumo pra avaliação:** este exercício apresenta dois conceitos novos — o método `.endswith()` (verifica sufixo de uma string) e a instrução `continue` (pula para a próxima iteração de um loop, ignorando o restante do bloco naquela volta) — usados juntos para filtrar e transformar uma lista de palavras.
