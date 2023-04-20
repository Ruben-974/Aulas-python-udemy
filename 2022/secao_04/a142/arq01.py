list = [
    'a', 5, 1.5, True, [0, 1, 2], (0, 1), {0, 1}, {'name': 'Jack'}
]

for item in list:

    if isinstance(item, (int, float)) and item != True:
        print(f'{item} is int/float')

    if isinstance(item, str):
        print(f'{item} is str')

    if isinstance(item, dict):
        print(f'{item} is dict')

