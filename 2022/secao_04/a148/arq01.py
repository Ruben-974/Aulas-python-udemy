# Yield from
def gen1():
    print('START GEN1')
    yield 1
    yield 2
    print('FINISH GEN1')


def gen2(gen=None):
    print('START GEN2')
    if gen is not None:
        yield from gen
    yield 3
    yield 4
    print('FINISH GEN2')


def gen3():
    print('START GEN3')
    yield 5
    yield 6
    print('FINISH GEN3')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()