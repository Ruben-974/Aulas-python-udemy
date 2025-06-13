from pprint import pprint

# dir, hasattr and getattr in Python

name = 'Jack'

pprint(dir(name))  # dir - Lists attributes and methods of an object

# hasattr - Checks if an attribute/method is present in an object

print(hasattr(name, 'capitalize'))

# Retrieves the value of an attribute/method from an object and executes it with *(parameters)

print(getattr(name, 'upper')())
