import copy

punter_1 = {
    'name': 'Jack',
    'years': 22,
    'numbers': [12, 15, 18, 25, 29]
}

#analytics = punter_1 # memory location
#analytics = punter_1.copy() # shallow copy
analytics = copy.deepcopy(punter_1) # deep copy

analytics['numbers'][0] = 5

print(analytics)
print(punter_1)