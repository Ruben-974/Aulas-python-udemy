import json


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = self.height = None

    def body(self, weight, height):
        self.weight = weight
        self.height = height


p1 = Person(None, None)

with open('arq01.json', 'r', encoding='utf-8') as arq:
    p1.__dict__ = json.load(arq)


print(p1.__dict__)
