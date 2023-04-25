def generator(start, end):
    while start < end:
        yield start
        start += 1


gen = generator(0, 10)

next(gen)
next(gen)
next(gen)
next(gen)
next(gen)

for number in gen:
    print(number)
