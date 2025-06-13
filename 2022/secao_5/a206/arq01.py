import json


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = self.height = None

    def body(self, weight, height):
        self.weight = weight
        self.height = height


p1 = Person('John', 25)
p1.body(79, 1.80)
print(p1.__dict__)

with open('arq01.json', 'w', encoding='utf-8') as arq:
    json.dump(p1.__dict__, arq, ensure_ascii=False, indent=4)
