from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

accumulator = 0
for num in numbers:
    accumulator += num

print(accumulator)
accumulator = 0

print(reduce(lambda ac, n: ac + n,
             numbers, 0))