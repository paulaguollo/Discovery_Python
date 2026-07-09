#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].lower())

#     O que muda em relação ao upcase_it.py
# Estruturalmente, nada muda — mesma validação (!= 2), mesma lógica de if/else. A única diferença é o método de string usado:

# .upper() → converte tudo para maiúsculas
# .lower() → converte tudo para minúsculas

# Ambos são métodos embutidos de string, seguem a mesma regra (retornam uma string nova, não alteram a original, porque strings são imutáveis em Python), e funcionam sobre qualquer caractere alfabético — números, espaços e pontuação (como o ! no terceiro exemplo) simplesmente não são afetados.
# Por que isso é importante destacar na avaliação
# Esse é um ótimo exemplo pra você mostrar que entendeu o padrão reutilizável: uma vez que você entende a estrutura "valida quantidade de parâmetros → aplica uma transformação de string → imprime", ela se repete em vários exercícios do módulo, só trocando qual método (.upper(), .lower(), .capitalize(), etc.) é chamado. Isso é o próprio espírito do módulo: aprender a manipular strings como se fossem arrays de caracteres, usando os métodos prontos que a linguagem já oferece, em vez de reinventar a lógica de conversão de maiúscula/minúscula na mão (percorrendo caractere por caractere).
