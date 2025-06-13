dictionary = dict()

dictionary = {
    'name': 'Jack',
    'surname': 'Pearson',
    'years': 19,
    'height': 1.72,
    'address': [
        {'road': '...', 'number': 123},
        {'road': '...', 'number': 321}
    ]
}

for key in dictionary:
    print(f'{key}: {dictionary[key]}')