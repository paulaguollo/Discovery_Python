#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1]
    word = input("What was the parameter? ")
    if word == param:
        print("Good job!")
    else:
        print("Nope, sorry...")

# ## O que o enunciado pedia

# > - O programa recebe uma string como parâmetro.
# > - Pede para o usuário digitar uma palavra que combine com o parâmetro passado.
# > - Mostra `"Good job!"` se bateu, `"Nope, sorry..."` se não bateu.
# > - Mostra `"none"` se o número de parâmetros for diferente de 1.

# Exemplo do PDF:
# ```
# ?> ./parameter_matching.py
# none
# ?> ./parameter_matching.py "Hello"
# What was the parameter? Bonjour
# Nope, sorry...
# ?> ./parameter_matching.py "Hello"
# What was the parameter? Hello
# Good job!
# ```

# ## `len(sys.argv) != 2`

# Mesma lógica do `upcase_it.py` do módulo anterior: o programa exige **exatamente 1** parâmetro. `sys.argv` teria `[nome_do_script, parametro]` = 2 itens; qualquer coisa diferente disso é inválido.

# ## `param = sys.argv[1]`

# Guarda o parâmetro passado (o "gabarito") numa variável com nome descritivo, `param`, em vez de ficar usando `sys.argv[1]` repetidamente no código — deixa mais legível.

# ## `input("What was the parameter? ")`

# Aqui está a **novidade principal** deste módulo em relação ao anterior: `input()`.

# Diferente de `sys.argv` (que pega valores passados **na hora de chamar o programa**, antes dele começar a rodar), `input()` **pausa a execução do programa** e espera o usuário digitar algo **enquanto o programa já está rodando**, apertando Enter para confirmar. A string dentro dos parênteses (`"What was the parameter? "`) é o **prompt** — o texto que aparece antes do cursor, convidando o usuário a digitar.

# `input()` sempre devolve o que foi digitado como uma **string** (mesmo que a pessoa digite números), e é isso que fica guardado em `word`.

# ## `if word == param:`

# Aqui é uma comparação simples de igualdade entre duas strings. O operador `==` compara **valor**, não identidade — ou seja, ele verifica se o conteúdo das duas strings é idêntico, caractere por caractere (incluindo maiúsculas/minúsculas: "Hello" é diferente de "hello"). Se bater, `True` → `"Good job!"`; senão, `False` → `"Nope, sorry..."`.

# ---

# **Resumo pra avaliação:** esse exercício é sobre a diferença entre **entrada via linha de comando** (`sys.argv`, valores fixados antes de o programa rodar) e **entrada interativa** (`input()`, que pausa a execução e espera o usuário digitar em tempo real). O resto — validação de quantidade de parâmetros e comparação de strings com `==` — já é familiar dos exercícios anteriores.
