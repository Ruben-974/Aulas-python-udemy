import json

directory_file = 'arq01.json'

class Person:

    def __init__(self, name, years):
        self.name = name
        self.years = years

p1 = Person('Mike', 29)
p2 = Person('Jon', 13)
p3 = Person('Max', 22)
p4 = Person('Mary', 18)

def execute():

    with open(directory_file, 'w', encoding='UTF8') as file:
        json.dump([p1.__dict__, p2.__dict__, p3.__dict__, p4.__dict__], file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('is the main')
    execute()
