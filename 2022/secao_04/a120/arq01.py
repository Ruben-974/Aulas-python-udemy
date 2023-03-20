person = {'name': 'Jack'}

person['surname'] = 'Jhon'
person['years'] = 27

del person['surname']

for i, k in person.items():
	print(f'{i}: {k}')


if person.get('surname') is None:
	print('surname no exist')

else:
	print('surname exist')
