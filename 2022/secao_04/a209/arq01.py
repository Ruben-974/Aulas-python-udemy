class Person:

    year = 2025

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def method_class(cls):
        print('hi')

    @classmethod
    def has_20_age(cls, name):
        return Person(name, 20)

    @classmethod
    def is_anonymous(cls, age):
        return 'Anonymous', age


p1 = Person.has_20_age('John')
print(p1.name, p1.age)


