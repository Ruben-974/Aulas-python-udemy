class Cart:

    def __init__(self):
        self._products = []

    def to_add_product(self, *products):
        self._products += products

    def list_products(self):
        for product in self._products:
            print(f'Product: {product.product} | Value: R${product.value}')

    def value_of_products(self):
        print(f'R${sum([product.value for product in self._products])}')

class Product:

    def __init__(self, product, value):
        self.product, self.value = product, value


cart = Cart()
cart.list_products()
p1, p2, p3 = Product('Pen', 2.2), Product('Book', 23.5), Product('Pencil', 1)
cart.to_add_product(p1, p2, p3)
cart.list_products()
cart.value_of_products()