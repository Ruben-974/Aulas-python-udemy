from itertools import groupby

def _key(notes):
    return notes['note']


notes = [
    {'name': 'Jack', 'note': 'B'},
    {'name': 'Jon', 'note': 'A'},
    {'name': 'Annie', 'note': 'C'},
    {'name': 'Peter', 'note': 'B'},
    {'name': 'Mick', 'note': 'A'},
    {'name': 'Maria', 'note': 'A'},
]


notes = sorted(notes, key=_key)
ordered = groupby(notes, key=_key)
for c in ordered:
    print(c[0])
    lista = c[1]
    for c1 in c[1]:
        print(c1['name'])