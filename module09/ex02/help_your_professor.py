#!/usr/bin/env python3

def average(scores):
    return sum(scores.values()) / len(scores)

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")


# .values() — pega só os valores do dict (ignora as chaves).
# sum() — soma os itens de um iterável, função embutida.
# / — divisão em Python 3 é sempre float (50/4 = 12.5), mesmo dividindo dois inteiros. Diferente de C/Java onde int/int trunca. Se quisesse divisão inteira, seria //.
