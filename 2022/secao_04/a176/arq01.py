from functools import partial

numbers = [1, 2, 3, 4, 5]

# We can multiply "n" by "n" using list comprehension, it can get complex and unreadable

numbersXnumbers = [n*n for n in numbers]
print(numbersXnumbers)


# Alternatively we can use map(), where you get a function and values to iterate over.
def mult(n1, n2):
    return n1 * n2


numbersXnumbers = list(map(mult, numbers, numbers))
print(numbersXnumbers)
