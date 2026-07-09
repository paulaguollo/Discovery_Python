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


Próximo: **Módulo 6 — Exercício 04 (scan_it.py)**, o mais denso desse módulo:

```python
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
```

# ## O que o enunciado pedia

# > - O programa recebe **2 parâmetros**: uma palavra-chave e um texto onde procurar.
# > - Deve mostrar **quantas vezes** a palavra-chave aparece no texto.
# > - Se o número de parâmetros for diferente de 2, **ou** se a palavra-chave não aparecer no texto, mostrar `"none"`.

# Exemplos do PDF:
# ```
# ?> ./scan_it.py | cat -e
# none$
# ?> ./scan_it.py "the" | cat -e
# none$
# ?> ./scan_it.py "the" "hello world" | cat -e
# none$
# ?> ./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
# 2$
# ```

# ## `import re`

# Aqui aparece um módulo novo: `re`, de **regular expressions** (expressões regulares) — uma "mini-linguagem" para buscar padrões dentro de texto. O próprio PDF dá a dica: *"you can use the `re.findall()` method"*.

# ## `len(sys.argv) != 3`

# Por que 3 e não 2? Porque agora temos **dois** parâmetros reais (a keyword e o texto), então `sys.argv` tem: `[nome_do_script, keyword, texto]` → 3 itens. Se vier qualquer coisa diferente de 3 (0, 1 ou mais de 2 argumentos), é inválido.

# ## `re.escape(keyword)`

# Esse é o detalhe mais sutil do exercício. Dentro de expressões regulares, certos caracteres têm **significado especial** (por exemplo, `.` significa "qualquer caractere", `*` significa "repetição", etc.). Se a palavra-chave do usuário tivesse algum desses caracteres por acaso, o `re.findall()` interpretaria errado.

# `re.escape()` pega a string e "neutraliza" esses caracteres especiais, tratando-os como texto literal. Isso garante que estamos procurando a palavra **exatamente como foi digitada**, e não como um padrão de regex.

# ## `re.findall(padrão, texto)`

# Essa função procura **todas as ocorrências** de um padrão dentro de uma string e devolve uma **lista** com cada ocorrência encontrada (não a posição, o texto encontrado mesmo). No exemplo:

# ```python
# re.findall("the", "the quick brown fox jumps over the lazy dog")
# # -> ["the", "the"]
# ```

# Ele encontra "the" no início da frase e depois em "over **the** lazy" — duas ocorrências como **substring** (não conta se é uma "palavra inteira" ou não; é busca de texto dentro de texto, por isso não conta "there" ou "them", mas contaria mesmo dentro de outra palavra, tipo "**the**y" também contaria como match).

# ## `len(matches) == 0`

# Depois de buscar, `matches` é uma lista. Se estiver vazia (`len == 0`), significa que a palavra-chave não apareceu nenhuma vez → mostra `"none"` (é o caso de `"the"` em `"hello world"`). Senão, mostra `len(matches)`, que é a contagem de ocorrências.

# ---

# **Resumo pra avaliação:** esse exercício junta duas validações no mesmo `"none"` — quantidade errada de parâmetros **ou** nenhuma ocorrência encontrada — e usa o módulo `re` para buscar substrings, com `re.escape()` garantindo que a busca seja literal (texto puro), não interpretada como padrão de regex.

