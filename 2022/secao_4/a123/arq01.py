person = {
    'name': 'Israel',
    'years': 18
}

print(person.get('surname'))
print(person.get('name'))
# years = person.pop('years') # similar to dell
# item = person.popitem()

print(person)

person.update({
    'name': 'Rúben',
    'surname': 'Israel'
})

person.update(cpf='000.000.000-00')

tuple_ = (('name', 'Jack'), ('years', '30'))

person.update(tuple_)

print(person)
