"""
Desempacotamento de listas em Python
"""

lista = ['Ruben', 'Pedro', 'Ana', 'Marcela', 'Clara', 'João']

n1, n2, *outros = lista

print(n1, n2, outros)

*outros, n1, n2 = lista

print(n1, n2, outros)

n1, *outros, n2 = lista

print(n1, n2, outros)
