class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name} eats {food}')


leao = Animal('Leão')
print(leao.name)
leao.eat('potato')
