person = {
    'name': 'Maria',
    'surname': 'Silva',
}

new_information = {
    'years': 17,
    'height': 1.67
}

person = dict(**person, **new_information)

print(person)

n, *rest = person.items()

def show(**kargs):
    for k, v in kargs.items():
        print(f'{k}: {v}')

show(**person)