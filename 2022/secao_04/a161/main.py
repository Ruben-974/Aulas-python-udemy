from package import products
from package.module import print_list
from copy import deepcopy


new_value = [
    {'name': c['name'], 'value': round(c['value']*1.1, 2)}
    for c in deepcopy(products)
]

sorted_by_name = deepcopy(products)
sorted_by_name.sort(key=lambda products: products['name'], reverse=True)

sorted_by_value = deepcopy(products)
sorted_by_value.sort(key=lambda products: products['value'])


print_list(products)
print_list(new_value)
print_list(sorted_by_name)
print_list(sorted_by_value)