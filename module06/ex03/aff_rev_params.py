#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) < 2:
    print("none")
else:
    for word in reversed(args):
        print(word)

Segue o **Módulo 6 — Exercício 03 (aff_rev_params.py)**:

```python
#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) < 2:
    print("none")
else:
    for word in reversed(args):
        print(word)
```

# Repare que com **1 parâmetro só** ("coucou") o programa também mostra `"none"` — é aí que mora a diferença deste exercício em relação aos anteriores.

# ## `sys.argv[1:]` — fatiamento (slicing)

# Essa é a primeira novidade importante. Em vez de acessar item por item (`sys.argv[1]`, `sys.argv[2]`...), uso **slicing**: `sys.argv[1:]` significa *"pegue a lista `sys.argv` a partir do índice 1 até o final"*. Isso cria uma **nova lista** contendo só os argumentos reais, já sem o nome do script (índice 0).

# Isso deixa o código mais limpo: a partir daqui, `args` já é "a lista de parâmetros que o usuário passou", sem precisar ficar descontando o índice 0 toda hora.

# ## `len(args) < 2`

# Aqui a regra do enunciado já é sobre `args` (não mais sobre `sys.argv` completo), então a lógica fica direta: se a lista de parâmetros reais tem **menos de 2** itens (0 ou 1), mostra `"none"`. É diferente do `upcase_it.py`, que exigia exatamente 1 — aqui o mínimo aceitável é 2, porque não faz muito sentido "inverter a ordem" de uma lista com só 1 elemento.

# ## `reversed(args)`

# Função embutida que devolve um **iterador reverso** — ou seja, permite percorrer a lista de trás para frente, sem precisar modificar a lista original nem criar uma cópia invertida na mão. É diferente de `args.reverse()` (que inverteria a lista *no lugar*, alterando `args` permanentemente) ou de `args[::-1]` (que cria uma cópia invertida usando slicing com passo negativo). Qualquer uma das três abordagens resolveria o exercício; usei `reversed()` porque é a mais direta para "só percorrer ao contrário".

# ## `for word in reversed(args): print(word)`

# Um `for` simples que percorre a versão invertida e imprime cada palavra numa linha própria — o `print()` já adiciona o `\n` de cada vez, então a saída bate certinho com o exemplo (`hello`, depois `piscine`, depois `Python`, cada um em sua própria linha).

# ---

# **Resumo pra avaliação:** esse exercício introduz **slicing** (`sys.argv[1:]`) para isolar os parâmetros reais e **`reversed()`** para percorrer uma lista de trás pra frente sem alterar a lista original — mostrando que em Python muitas vezes existe uma função pronta pra evitar escrever um loop manual de inversão.
