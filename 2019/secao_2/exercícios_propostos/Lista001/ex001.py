"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        print(f'{num} é um número par!')
    else:
        print(f'{num} é um número ímpar!')
except:
    print('Erro: Digite um número inteiro!')
