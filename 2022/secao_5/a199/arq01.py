# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person('Marks', '22')
person2 = Person('Lily', '20')

print(person1.name, person1.age)
print(person2.name, person2.age)


