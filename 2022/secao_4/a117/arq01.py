def multiplier(multiply):
    def calculate(number):
        return number * multiply
    return calculate


duplicate = multiplier(2)
triplicate = multiplier(3)
quadruplicate = multiplier(4)

print(duplicate(5))
print(triplicate(5))
print(quadruplicate(5))