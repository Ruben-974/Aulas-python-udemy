"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

cpf = '087630362900'  # input('Digite um CPF: ')

if '.' in cpf or '-' in cpf:
    for c in '.-':
        cpf = cpf.replace(c, '')

if not cpf.isnumeric() or len(cpf) > 11:
    print('ERRO: Digite somente números de 11 dígitos')
    exit()

new_cpf = cpf[:-2]

for c in range(10, 12):

    soma = 0

    for i, v in enumerate(range(c, 1, -1)):
        soma += int(new_cpf[i]) * v

    ver1 = 11 - (soma % 11)

    new_cpf += '0' if ver1 > 9 else str(ver1)

msg = 'CPF valido' if cpf == new_cpf else 'CPF invalido'

print(msg)
