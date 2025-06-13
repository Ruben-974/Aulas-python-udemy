from pprint import pprint

numbers = [
    (x, y)
    for x in range(3)
    for y in range(3)

]

pprint(numbers, width=10)
