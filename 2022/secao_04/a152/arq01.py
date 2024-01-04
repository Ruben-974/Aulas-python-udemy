def division(x, y):

    for z in (x, y):
        no_zero(z)
    
    return(x/y)


def no_zero(x):

    if x == 0:
        raise ZeroDivisionError('Zero not is divisible')


print(division(1, 0))