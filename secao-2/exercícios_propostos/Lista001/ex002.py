"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    hr = int(input('Qual é a hora neste momento? [0-23]: '))
except:
    print('Erro: Digite um número inteiro!')
else:
    if 0 <= hr <= 11:
        print('Bom dia!')
    elif 12 <= hr <= 17:
        print('Boa tarde!')
    elif 18 <= hr <= 23:
        print('Boa noite!')
    elif hr > 23 or hr < 0:
        print('Erro: Digite um número entre 0 e 23!')