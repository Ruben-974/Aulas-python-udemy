class Car:

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = str(year)[-2:]+'s'

    def accelerate(self):
        print(f'{self.model} is accelerating...')

    def decelerate(self):
        print(f'{self.model} is decelerating...')


car1 = Car('Beetle', 'Blue', 1970)
car2 = Car('Civic', 'Black', 1990)

print(car1.model, car1.color, car1.year)
car1.accelerate()
car1.decelerate()

print(car2.model, car2.color, car2.year)
car2.accelerate()
car2.decelerate()
