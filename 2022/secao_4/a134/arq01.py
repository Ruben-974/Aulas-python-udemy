def execute(function, *args):
    return function(*args)

def soma(x, y):
    return x + y

def create_multiplier(multipler):
    def multuply(number):
        return number * multipler
    return multuply

result = execute(
    lambda x, y: x + y,
    9, 2
)

print(result)

result = execute(
    lambda m: lambda n: n * m,
    5
)

print(result(7))