from pprint import pprint

product = {
    'name': 'pen',
    'price': 2.5,
    'category': 'desk'
}

new_product = {
    key: value.upper()
    if type(value) == str else value
    for key, value in product.items()
    if key != 'category'
}

pprint(new_product, width=20)