def sum(x, y):
    return x + y


def mult(x, y):
    return x * y


def creat_function(function, x):

    def internal(y):
        return function(x, y)
    return internal

sum_10 = creat_function(sum, 10)
mult_10 = creat_function(mult, 10)

print(sum_10(5))
print(mult_10(9))

