from typing import TYPE_CHECKING, List
from Models.Entities.Employee import Employee

if TYPE_CHECKING:
    from Models.Entities.Client import Client


class Cashier(Employee):
    def __init__(self, id: str, name: str, age: int, phone_number: str, employee_number: str, desk_number: int):
        super().__init__(id, name, age, phone_number, employee_number)
        self._desk_number = desk_number

    def purchase_client_products(self, client: 'Client'):
        from Models.Tools.FileHandler import FileHandler
        client_wishlist = client.get_wishlist()
        FileHandler.append_products_to_file(f"../PythonFinal/Files/Clients/{client.get_id()}/existing_products.txt",
                                            client, client_wishlist)

    def sell_to_client(self):
        from Models.Tools.FileHandler import FileHandler
        clients = FileHandler.read_clients("../PythonFinal/Files/Clients")
        from Models.Tools.Tools import Tools
        for i in range(0, len(clients)):
            print(Tools.client_purchase(f"           Client number {i + 1}          "))
            clients[i].display_client()
            print("")

        chosen_client = int(input("Choose client number: ")) - 1
        client = clients[chosen_client]

        sum_price = 0
        if len(clients[chosen_client].get_wishlist()) == 0:
            print(f"{client.get_name()} has no items on the cart.")
        else:
            print(Tools.client_purchase(f"           Client Products"))
            for product in client.get_wishlist():
                print(Tools.cashier_background(f"- {product.get_name()} (${product.get_price()})"))
                sum_price += product.get_price()

            proceed = input(f"Total for purchase: ${sum_price} would you like to proceed? y/n: ")
            if proceed == 'y':
                from Models.Inanimates.Purchase import Purchase
                new_purchase = Purchase(client, self)
                from Models.Tools.FileHandler import FileHandler
                FileHandler.append_products_to_file(
                    f"../PythonFinal/Files/Clients/{client.get_id()}/existing_products.txt",
                    client, client.get_wishlist())
                FileHandler.add_purchase(new_purchase)
                return new_purchase

    def __str__(self):
        return f"{self._id},{self._name},{self._age},{self._phone_number},{self._employee_number},{self._desk_number}\n"
