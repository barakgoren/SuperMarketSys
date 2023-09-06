from Models.Entities import Client
from typing import List
from Models.Inanimates.Product import Product
from Models.Entities.Cashier import Cashier
from Models.Tools.Tools import Tools
from Models.Entities.Employee import Employee


class Purchase:

    def __init__(self, buyer: Client, cashier: Employee):
        self._date = Tools.get_current_time()
        self._buyer: Client = buyer
        self._cashier: Employee = cashier
        self._products: List[Product] = buyer.get_wishlist()
        self._total_price: float = 0
        for product in self._products:
            self._total_price = float(self._total_price) + float(product.get_price())


    def get_total(self):
        return self._total_price

    def get_products(self):
        return self._products

    def get_client(self):
        return self._buyer

    def __str__(self):
        return f"{self._date}^{self._buyer.get_name()}^{self._cashier.get_name()}^{self._total_price}"
