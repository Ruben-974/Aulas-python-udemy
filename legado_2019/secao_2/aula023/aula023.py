"""
Split, Join, Enumerate em Python

* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista #  list
"""

txt = 'O Brasil é o país do futebol, o Brasil é penta.'
lista = txt.split()

for i, v in enumerate(lista):
    print(i, v)


