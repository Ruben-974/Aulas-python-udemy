import json

givens = {
    'Numbers': [1, 2, 3, 4, 5],
    'string': 'Txt',
    'negative_nums': (-1, 0, 1),
    'mult_nums': [2*8, 2*7],
    'persons': {'Name': 'Jack', 'Age': 18},
}

with open('arq.json', 'w', encoding='utf8') as arq:
    json.dump(givens, arq, ensure_ascii=False, indent=4)

