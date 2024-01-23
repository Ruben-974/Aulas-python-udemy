# copy, sorted, produtos.sort
# Exercícios

from copy import deepcopy

def prt(lt):

    for c in lt:
        print(c)
    print('\n')

products = [
    {'name': 'product 1', 'value': 9.4},
    {'name': 'product 2', 'value': 3.7},
    {'name': 'product 3', 'value': 2.0},
    {'name': 'product 4', 'value': 6.0},
    {'name': 'product 5', 'value': 9},
]

prt(products)

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

new_value = deepcopy(products)

for c in range(len(new_value)):
    new_value[c]['value'] = float(f'{new_value[c]["value"]*1.1:.2f}')

prt(new_value)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

sorted_by_name = deepcopy(products)
sorted_by_name.sort(key=lambda products: products['name'], reverse=True)

prt(sorted_by_name)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

sorted_by_value = deepcopy(products)

sorted_by_value.sort(key=lambda products: products['value'])

prt(sorted_by_value)

