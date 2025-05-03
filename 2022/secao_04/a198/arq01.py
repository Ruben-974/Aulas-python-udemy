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
    ...


person1 = Person()
person2 = Person()

person1.name = 'Pedro'
person1.age = 25

person2.name = 'Maria'
person2.age = 22

print(person1.name)
print(person1.age)
print()
print(person2.name)
print(person2.age)



