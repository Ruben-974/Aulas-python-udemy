def salutation(name, message):
    return f'Hey {name}, {message}!'

def execute(function, *args):
    return function(*args)


result = execute(salutation, 'Rúben', 'good morning')

print(result)