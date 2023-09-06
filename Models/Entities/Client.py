from typing import List, TYPE_CHECKING
from Models.Inanimates.Product import Product
from Models.Entities.Person import Person

if TYPE_CHECKING:
    from Cashier import Cashier


class Client(Person):

    def __init__(self, id: str, name: str, age: int, phone_number: str, wanted_products: List[Product],
                 existing_products: List[Product]):
        super().__init__(id, name, age, phone_number)
        self._wanted_products: List[Product] = wanted_products
        self._existing_products: List[Product] = existing_products

    def add_product(self, product: Product):
        self._wanted_products.append(product)

    def purchase_wishlist(self, cashier: 'Cashier'):
        cashier.purchase_client_products(self)

    def set_wishlist(self, wish_list: List[Product]):
        self._wanted_products = wish_list

    def get_existing_products(self):
        return self._existing_products

    def get_wishlist(self):
        return self._wanted_products
    #
    # def get_name(self):
    #     return self.get_name()

    def display_client(self):
        from Models.Tools.Tools import Tools
        print(Tools.client_background(f"Client Name: {self._name}"))
        print(Tools.client_background(f"Client ID: {self._id}"))
        print(Tools.client_background(f"Client Phone Number: {self._phone_number}"))

    def str(self):
        pass

    def eql(self):
        pass
