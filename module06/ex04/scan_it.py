#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    matches = re.findall(re.escape(keyword), text)
    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))



#  importa o sys, para acessar os argumentos digitados no terminal, e o re, para fazer buscas com expressões regulares. 

# o re.escape é usado para tratar a palavra-chave como texto literal, evitando que caracteres especiais (como . ou *) sejam interpretados como parte de um padrão regex.  caso contrário, imprime o número de vezes que a palavra-chave apareceu. Vale notar que a busca diferencia maiúsculas de minúsculas e conta substrings, não palavras inteiras isoladas — ou seja, buscar "gat" também contaria ocorrências dentro de "gato" ou "gata".