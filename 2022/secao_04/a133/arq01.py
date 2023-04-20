list = [
    {'name': 'Maria', 'surname': 'Oliveira'},
    {'name': 'Daniel', 'surname': 'Silva'},
    {'name': 'Eduardo', 'surname': 'Moreira'}
]

list.sort(key=lambda item:item['name'])
print(list)