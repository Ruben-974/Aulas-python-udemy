"""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

palavra = 'abelha'
letras = []
cont = 3

while True:

    palavra_tent = ''

    l = input('Digite uma letra: ')

    if len(l) > 1 or len(l) == 0:
        print('ERRO: Digite apenas uma letra!')
        continue

    if l in palavra:
        print(f'A letra {l} está na palavra secreta!')
        letras.append(l)
    else:
        print(f'A letra {l} não está na palavra secreta!')
        cont -= 1
        if cont == 0:
            print('Acabou suas chances... GAME OVER!')
            break

    for c in palavra:
        if c in letras:
            palavra_tent += c
        else:
            palavra_tent += '_'

    print(F'A palavra por enquanto está "{palavra_tent}" e você tem {cont}')

    if palavra_tent == palavra:
        print('VOCÊ VENCEU!')
        break

    print()
