"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Qual o seu nome? ')
ctr = len(nome)
if ctr <= 4:
    print(f'{nome} é um nome curto!')
elif ctr <= 6:
    print(f'{nome} é um nome normal!')
elif ctr > 6:
    print(f'{nome} é um nome grande')

