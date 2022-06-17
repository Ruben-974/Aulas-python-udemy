"""
For / Else em python
"""

lista = ['Rúben', 'Luis', 'José']

for c in lista:
    if c[0].lower() == 'p':
        break
    print(c)
else:
    print('Não existe palavra com a letra "p"')

