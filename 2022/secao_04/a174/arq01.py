# Combinations, Permutations and Product - Itertools
# Combination - Order not important
# Permutation - Order is important
# Product - Order imports and repeats unique values

from itertools import combinations, permutations, product


def format(iterable):
    print(*iterable, sep='\n')
    print()


person = ['Jack', 'Anne', 'Julie', 'Marks']
shirt = [['white', 'black'],
         ['P', 'M', 'G'],
         ['Man', 'Woman', 'unisex']]

combination_persons = combinations(person, 2)
format(combination_persons)
combination_persons = permutations(person, 2)
format(combination_persons)
combination_shirt = product(*shirt)
format(combination_shirt)

