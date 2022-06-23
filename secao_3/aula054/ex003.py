"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""


def soma_porcentagem(n1, n2):
    return n1+(n1*n2/100)


print(soma_porcentagem(70, 50))
