#  Conceitos Python (Módulos 6, 7, 8, 9)

## Módulo 6 e 7 — Parâmetros de linha de comando

**`sys.argv`**
- Lista com os argumentos passados na chamada do script.
- `sys.argv[0]` é SEMPRE o nome do script — nunca um parâmetro real.
- `sys.argv[1:]` (slicing) isola só os parâmetros reais, sem o nome do script.
- Tudo em `sys.argv` é **string**, mesmo que pareça número (`"10"`, não `10`).

**Validação de quantidade de parâmetros — atenção à regra exata:**
| Regra do enunciado | Condição |
|---|---|
| Exatamente 1 parâmetro | `len(sys.argv) != 2` |
| Exatamente 2 parâmetros | `len(sys.argv) != 3` |
| Pelo menos 1 (extras ok) | `len(sys.argv) < 2` |
| Pelo menos 2 (extras ok) | `len(args) < 2` (com `args = sys.argv[1:]`) |
| Zero parâmetros = erro | `len(args) == 0` |

**`int(sys.argv[1])`** — conversão de tipo (type casting). Necessário para comparar/operar numericamente, já que `sys.argv` só entrega strings.

## Strings — métodos e comportamento

- Strings são **imutáveis**: `.upper()`, `.lower()`, `.capitalize()` sempre retornam uma string **nova**, nunca alteram a original.
- Strings são **iteráveis**: `for char in string` percorre caractere por caractere, igual a percorrer uma lista.
- `.endswith(sufixo)` — testa se a string termina com determinado texto.
- Slicing: `string[:8]` pega os primeiros 8 caracteres; `[start:end]` sempre exclui o índice `end`.
- Comparação `==` entre strings é sensível a maiúsculas/minúsculas (case-sensitive).
- f-strings: `f"{variavel}"` interpola valores direto no texto.

## Controle de fluxo

- `continue` — pula o resto do bloco atual e vai direto pra próxima iteração do loop.
- `for` itera diretamente sobre os **itens** de uma coleção (lista, string, dict) — não precisa de índice/contador manual como o `while`.
- `range(a, b)` **exclui** `b` — para incluir o limite superior, usar `range(a, b + 1)`.
- `range()` sozinho é um objeto "preguiçoso" (não é lista ainda) — `list(range(...))` força a materialização.

## Módulo 8 — Funções

- `def nome(parametros):` define a função; só executa quando **chamada** (`nome()`).
- Parâmetro com valor default: `def f(x="valor"):` — usado quando a função é chamada sem esse argumento.
- `return` devolve um valor e encerra a função (diferente de só usar `print()` dentro dela).
- `isinstance(valor, tipo)` — checagem de tipo em runtime (Python não tem tipagem estática).

**Escopo (scope) — o ponto mais conceitual do módulo:**
- Parâmetros de função recebem uma **cópia** do valor (para tipos imutáveis como `int`, `str`).
- Alterar o parâmetro dentro da função **não** afeta a variável original de fora.
- Para "propagar" a mudança, é preciso reatribuir o retorno: `my_var = add_one(my_var)`.
- (Isso é diferente para tipos mutáveis como listas/dicts, onde métodos como `.append()` alteram o objeto original porque mexem na mesma referência de memória.)

## Módulo 9 — Dicionários (dict)

- Equivalente a hash map / objeto: pares chave-valor.
- `.keys()` — só as chaves. `.values()` — só os valores. `.items()` — pares `(chave, valor)`.
- `for chave, valor in dict.items():` — unpacking automático dos pares no loop.
- Dicionários podem ser aninhados: um valor pode ser outro dicionário.

**Programação funcional:**
- `lambda parametro: expressao` — função anônima de uma linha (equivalente a arrow function).
- `filter(funcao, iteravel)` — mantém só os itens em que a função retorna `True`. Retorna objeto preguiçoso → precisa de `list()` para virar lista de fato.
- `sorted(iteravel, key=funcao)` — ordena qualquer iterável; `key` define por qual critério ordenar. Não altera o original, retorna uma cópia ordenada.
- `sum(iteravel)` — soma os itens.

**Divisão em Python 3:**
- `/` sempre retorna `float`, mesmo com dois inteiros (`10 / 4 = 2.5`).
- `//` é divisão inteira (trunca).

## Padrões que se repetem (bom pra generalizar na avaliação)

1. **Validar entrada primeiro** (`if len(...) != X: print("none")`), só processar no `else`.
2. **Acumulador**: variável iniciada vazia/zero, que vai sendo atualizada dentro de um loop (`result += ...`).
3. **Separar "definir" de "chamar"**: funções só rodam quando chamadas, mesmo já definidas antes.
4. Python resolve muita coisa com **métodos prontos** (`.upper()`, `.endswith()`, `filter()`, `sorted()`) em vez de loops manuais — vale sempre citar a alternativa "na unha" pra mostrar que você entende o que o método faz por baixo.