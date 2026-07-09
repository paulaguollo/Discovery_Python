#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
else:
    print(sys.argv[1])

#len(sys.argv) < 2 → isso testa se não veio nenhum parâmetro real. 

# Lembra que sys.argv[0] é sempre o nome do script, então "nenhum parâmetro" = sys.argv só tem 1 item (len == 1), que é < 2. Isso cobre o caso none$ do primeiro exemplo.

 # else: print(sys.argv[1]) → se chegou aqui, é porque tem pelo menos 1 parâmetro real (pode ter mais, como no segundo exemplo com 3). 

# O código pega só sys.argv[1], que é sempre o primeiro parâmetro passado, e ignora sys.argv[2], sys.argv[3] etc. Isso é exatamente por que "Numeric" e "42" não aparecem no output, o enunciado só pediu o primeiro.
