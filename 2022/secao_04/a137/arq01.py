products = [
    {'name': 'p1', 'value': 20},
    {'name': 'p2', 'value': 10},
    {'name': 'p3', 'value': 30},
]

new_products = [
    {**product, 'value': product['value']*1.05} 

    
    if product['value'] > 20 else {**product}
    for product in products 
]

for c in new_products:
    print(c)