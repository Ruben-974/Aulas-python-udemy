class Manufacturer:

    def __init__(self, name):
        self.name = name
        self.car = None

    def car_for_manufacturer(self, car_):
        self.car = car_

class Car:

    def __init__(self, name):
        self.name = name
        self.engine = None

    def engine_for_car(self, engine_):
        self.engine = engine_

class Engine:

    def __init__(self, name):
        self.name = name


doblo = Car('Doblo')
engine = Engine('Engine Max')
uno = Manufacturer('Uno')

doblo.engine_for_car(engine)
uno.car_for_manufacturer(doblo)

print(uno.name)
print(uno.car.name)

engine.name = 'Engine Pro'

print(uno.car.engine.name)
