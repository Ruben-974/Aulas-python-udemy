"""x = 0

def sum_numbers(x):

    def sum(y):

        nonlocal x

        x += y

        return x

    return sum

 
sum_in_nine = sum_numbers(9)
print(sum_in_nine(4))
print(sum_in_nine(7))"""

x = 5

def sum(y):

    x += y

    return x

print(x)

sum(9)

print(x)