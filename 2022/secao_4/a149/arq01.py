try:

    x = 1
    y = 2
    z = x/y

except ZeroDivisionError:

    print('Zero is not divisible')

except TypeError:

    print("It's not a number")

print(z)