from typing import List
from Models.Inanimates.Product import Product
from Models.Tools.Tools import Tools


class PurchaseDisplay:

    def __init__(self, date: str, buyer: str, cashier: str, total_price: float, products: List[Product]):
        self._date = date
        self._buyer: str = buyer
        self._cashier: str = cashier
        self._total_price: float = total_price
        self._products: List[Product] = products

    def display_purchase(self):
        print("-------------------------------")
        print(Tools.purchase_background(f"Time: {self._date}"))
        print(Tools.purchase_background(f"Client name: {self._buyer}."))
        print(Tools.purchase_background(f"Cashier name: {self._cashier}."))
        print(Tools.purchase_background("Products:"))
        print(Tools.purchase_background(""))
        for product in self._products:
            # print(Tools.purchase_background(f"- {product.get_name()} (${product.get_price()})"))
            print(Tools.purchase_background_total(product, 0))
        print(Tools.purchase_background(""))
        print(Tools.purchase_background(f"Total is:               ${self._total_price}"))

    def get_total(self):
        return self._total_price
