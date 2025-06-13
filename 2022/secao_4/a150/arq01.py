try:

    x = 3
    y = 0
    z = x/y

except (TypeError, ZeroDivisionError) as error:

    print(f'MSG: {error}')
    print(f'ERROR: {error.__class__.__name__}')

print('Pass')