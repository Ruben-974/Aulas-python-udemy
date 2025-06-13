from random import randint

cpf = str(randint(10**8, 999999999))

for c in range(10, 12):

    soma = 0

    for i, v in enumerate(range(c, 1, -1)):
        soma += int(cpf[i]) * v

    ver1 = 11 - (soma % 11)

    cpf += '0' if ver1 > 9 else str(ver1)

print(cpf)
