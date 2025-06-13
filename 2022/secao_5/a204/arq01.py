# Atributos de Classes

class Person:

    year = 2025

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def year_of_birth(self):
        return Person.year - self.age


p1 = Person('John', 28)
p2 = Person('Mike', 14)

print(f'{p1.name} was born in {p1.year_of_birth()}')
print(f'{p2.name} was born in {p2.year_of_birth()}')
