from functools import partial

def mult(n1):
    return n1 * 5

teste = mult()

print(list(map(teste, [1, 2, 3])))