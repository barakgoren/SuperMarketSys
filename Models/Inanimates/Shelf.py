from typing import List
from Models.Inanimates import Product


class Shelf:
    def __init__(self, name: str, products: List[Product]):
        self._name: str = name
        self._products: List[Product] = products

    def get_name(self):
        return self._name

    def get_product(self):
        return self._products

    def display_shelf(self):
        from Models.Tools.Tools import Tools
        print(Tools.shiftmanager_background(f"             {self._name} Shelf"))
        for product in self._products:
            print(Tools.print_products(product, -2))
        print()

    def __str__(self):
        print(self._name)
        for product in self._products:
            print(product.get_name())
