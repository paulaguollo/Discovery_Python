#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].upper())


# Por que != 2 e não < 2 como no exercício anterior?
# Esse é justamente o ponto de comparação que citei antes. Aqui o enunciado diz explicitamente: "se o número de parâmetros for diferente de 1" — ou seja, o programa só aceita exatamente 1 parâmetro, nem 0, nem 2, nem mais.
# Como sys.argv[0] sempre é o nome do script, "exatamente 1 parâmetro real" significa len(sys.argv) == 2 (nome do script + 1 argumento). Por isso a condição de erro é != 2: qualquer coisa diferente de exatamente 2 itens em sys.argv cai no "none".
# Isso é diferente do aff_first_param.py, onde parâmetros extras eram permitidos (só o primeiro era usado). Aqui, se você chamar ./upcase_it.py "a" "b", o programa deveria recusar (mostrar "none"), porque o enunciado quer só 1 string, não uma lista de strings.
# sys.argv[1].upper()

# sys.argv[1] → pega a string passada (o primeiro e único argumento válido, já que garantimos que existe exatamente 1).
# .upper() → é um método de string embutido no Python. Toda string tem métodos prontos para manipulação, e .upper() retorna uma nova string com todos os caracteres convertidos para maiúsculas (não altera a original — strings em Python são imutáveis, ou seja, uma vez criadas não podem ser modificadas "no lugar"; qualquer operação como .upper() cria e devolve uma string nova).