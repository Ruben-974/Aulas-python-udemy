"""
while / else

contadores
acumuladores
"""

cont = acum = 0

while cont <= 10:
    print(cont, acum)
    cont += 1
    acum += cont

    if cont > 5:
        pass
else:
    print('Chegui no else!')

print('Fim do programa!')