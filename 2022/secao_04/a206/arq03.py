import json
import os


def open_json(file, values):

    with open(file, 'w', encoding='utf-8') as arq_json:
        json.dump(values, arq_json, ensure_ascii=False, indent=4)


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = self.height = None

    def body(self, weight, height):
        self.weight = weight
        self.height = height


if not os.path.isfile('arq01.json'):
    open_json('arq01.json', {})

p1 = Person('John', 34)
p1.body(67, 1.75)

open_json('arq01.json', p1.__dict__)


with open('arq01.json', 'r', encoding='utf-8') as arq:
    p1.__dict__ = json.load(arq)


print(p1.__dict__)
