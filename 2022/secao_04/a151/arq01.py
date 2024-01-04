try:

    print('start')
    
    x, y = 8, ''
    x/y
    
except ZeroDivisionError:

    print('Zero not is divisible')

except ValueError as error:

    print(f'ERROR: {error.__class__.__name__}')

else:

    print('No errors')

finally:

    print('Finally')

