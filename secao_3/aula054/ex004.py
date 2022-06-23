"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""


def FizzBuzz(n):

    msg = ''

    if n % 3 == 0:
        msg += 'Fizz'
    if n % 5 == 0:
        msg += 'Buzz'

    return msg if msg else n


for c in range(1, 101):
    print(FizzBuzz(c))
