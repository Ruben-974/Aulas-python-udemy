class Pessoa:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Client(Pessoa):
    ...

class Student(Pessoa):
    ...


s = Student('Mike', 'John')
print(s.name, s.surname)
c = Client('Marks', 'Heitor')
print(c.name, c.surname)

