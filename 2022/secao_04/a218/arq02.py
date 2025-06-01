class Car:

    def __init__(self, name):
        self._name = name
        self._engine = None
        self._manufacturer = None

    @property
    def name(self):
        return self._name

    @property
    def engine(self):
        return self._engine

    @property
    def manufacturer(self):
        return self._manufacturer

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

class Manufacturer:

    def __init__(self, name):
        self.name = name

class Engine:

    def __init__(self, name):
        self.name = name


engine = Engine('1.2')

fusca = Car('Fusca')
fusca.manufacturer = Manufacturer('Volkswagen')
fusca.engine = engine

doblo = Car('Doblo')
doblo.manufacturer = Manufacturer('Fiat')
doblo.engine = engine

print(fusca.manufacturer.name, fusca.name, fusca.engine.name)
print(doblo.manufacturer.name, doblo.name, doblo.engine.name)