#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    string = sys.argv[1]
    result = ""
    for char in string:
        if char == "z":
            result += "z"
    if result == "":
        print("none")
    else:
        print(result)


# ## O que o enunciado pedia

# > - O programa recebe uma string como parâmetro.
# > - Mostra `"z"` para cada ocorrência do caractere `"z"` na string, seguido de newline.
# > - Se o número de parâmetros for diferente de 1, **ou** se não houver nenhum `"z"` na string, mostra `"none"`.

# Exemplo do PDF:
# ```
# ?> ./string_are_arrays.py "The character Z is not found in this string" | cat -e
# none$
# ?> ./string_are_arrays.py "The character z is found in this string" | cat -e
# z$
# ?> ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
# zzz$
# ```

# ## O conceito central: **strings são iteráveis, como arrays**

# Esse é o nome do próprio exercício (*"Understanding Strings as Arrays"*) e a dica do PDF confirma: *"Strings are also composed of individual characters, just like arrays."*

# Em Python, uma string não é um bloco indivisível — ela é uma **sequência ordenada de caracteres**, e por isso pode ser percorrida com `for`, exatamente como faríamos com uma lista:

# ```python
# for char in string:
# ```

# A cada volta do laço, `char` recebe **um caractere** da string, na ordem em que aparecem. Isso é o mesmo princípio de `for word in args` do exercício anterior — só que ali percorríamos itens de uma lista, aqui percorremos caracteres de uma string.

# ## Diferenciando maiúsculas de minúsculas

# Repare que `"Zaz visits..."` tem um "Z" maiúsculo no início, mas o resultado é `zzz` (3 minúsculos), não 4. Isso acontece porque a comparação `char == "z"` é **sensível a maiúsculas/minúsculas** (case-sensitive): `"Z" != "z"` em Python. O `Z` maiúsculo do começo de "Zaz" e do nome "Zazie" não conta — só os `z` minúsculos contam. Por isso o segundo exemplo (`"The character Z..."`, com Z maiúsculo) dá `"none"`: não tem nenhum `z` minúsculo ali.

# ## `result = ""` e `result += "z"`

# Aqui uso o padrão de **acumulador**: começo com uma string vazia e vou **concatenando** (`+=`) um `"z"` a cada vez que encontro a condição. Isso é parecido com o padrão de "somar numa variável" (`soma += valor`) que você talvez já tenha visto em outras linguagens, só que aqui acumulando texto em vez de número.

# Importante lembrar: como strings são **imutáveis** em Python, `result += "z"` na verdade não está "adicionando" ao mesmo objeto — está **criando uma string nova** a cada iteração e reatribuindo o nome `result` a ela. Funciona perfeitamente, só é bom saber explicar isso se perguntarem "mas strings não eram imutáveis? como você está modificando ela então?" — a resposta é: você não está modificando, está substituindo por uma nova a cada passo.

# ## O `if result == "": print("none")` final

# Depois do loop, `result` contém todos os "z"s encontrados (ou nada, se não achou nenhum). Testamos se ficou **vazia** (`""`) para decidir entre `"none"` e mostrar o resultado — cobrindo a segunda condição do enunciado ("se não houver nenhum z").

# ---

# **Resumo pra avaliação:** o ponto-chave deste exercício é que **strings em Python são sequências iteráveis de caracteres**, assim como listas — por isso dá pra usar `for char in string` diretamente, sem precisar de índices. O resto é o padrão de acumulador (`result += "z"`) e duas checagens combinadas no mesmo `"none"`.
