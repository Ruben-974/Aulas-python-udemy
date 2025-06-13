numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([n for n in numbers if n%2 != 0])

print(list(filter(lambda n: n%2 != 0, numbers)))