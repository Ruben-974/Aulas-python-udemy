person = {
    'name': 'Rúben',
    'surname': 'Israel',
    #'years': 18
}

print(f'Quantity of items: {len(person)}')
print(f'Keys that exist: {tuple(person.keys())}')
print(f'Values that exist: {tuple(person.values())}')
print(f'Keys and values that exist: {tuple(person.items())}')

person.setdefault('years', 18)

print(f'Keys and values that exist: {tuple(person.items())}')