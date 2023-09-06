from typing import List
from Models.Entities.Employee import Employee
from Models.Entities.Sadran import Sadran
from Models.Entities.Client import Client
from Models.Interfaces.ILogistic import ILogistic
from Models.Inanimates.Product import Product
from Models.Inanimates.Shelf import Shelf
from Models.Inanimates.PurchaseDisplay import PurchaseDisplay


class ShiftManager(Employee, ILogistic):

    def __init__(self, id: str, name: str, age: int, phone_number:str, employee_number: str, employees: List[Employee],
                 hourly_salary: float):
        super().__init__(id, name, age, phone_number, employee_number)
        self._employees: List[Employee] = employees
        self._hourly_salary: float = hourly_salary

    def get_salary(self):
        return self._hourly_salary

    def get_workers(self):
        return self._employees

    def add_product(self, shelves: List[Shelf]):
        try:
            print("Choose shelf:")
            for i in range(0, len(shelves)):
                print(f"{(i + 1)}. {shelves[i].get_name()}")
            print("-------------------------------\n> ")
            shelf_choose = int(input()) - 1

            shelf = shelves[shelf_choose]
            print("All existing products:")
            for i in range(0, len(shelf.get_product())):
                print(f"{i + 1}. {shelf.get_product()[i].get_name()} (${shelf.get_product()[i].get_price()})")

            print("-------------------------------")
            print("Add product details:")
            new_product_category = input("Category: ")
            new_product_name = input("Name: ")
            try:
                new_product_price = float(input("Price: "))
            except BaseException:
                print("Must enter float: Price was set to 0.0")
                new_product_price = 0.0
            print("-------------------------------")
            from Models.Tools.FileHandler import FileHandler
            new_product = Product(new_product_category, new_product_name, new_product_price)
            FileHandler.add_product_to_shelf(new_product, shelf)
            print(f"Product Added: {new_product.get_name()} (${new_product.get_price()})")
        except BaseException:
            return

    def remove_product(self, shelves: List[Shelf]):
        print("Choose shelf:")
        for i in range(0, len(shelves)):
            print(f"{(i + 1)}. {shelves[i].get_name()}")
        print("-------------------------------")
        shelf_choose = int(input("> ")) - 1

        shelf = shelves[shelf_choose]
        print("Which product would you like to remove?: ")
        for i in range(0, len(shelf.get_product())):
            print(f"{i + 1}. {shelf.get_product()[i].get_name()} (${shelf.get_product()[i].get_price()})")

        print("-------------------------------")
        choosen_product_index = int(input("> ")) - 1
        choosen_product = shelf.get_product()[choosen_product_index]
        from Models.Tools.FileHandler import FileHandler
        FileHandler.remove_product_from_shelf(choosen_product, shelf)
        print("-------------------------------")
        print("Product removed!")

    def see_all_purchases(self, purchases: List[PurchaseDisplay]):
        sum_price: float = 0
        if len(purchases) != 0:
            for purchase in purchases:
                purchase.display_purchase()
                sum_price = sum_price + purchase.get_total()
        else:
            print("No purchases has done yet!")

        print(f"Total income until now for today: ${sum_price}")

    def add_sadran(self):
        from Models.Tools.FileHandler import FileHandler
        name = input("Please enter new sadran name: ")
        id = input("Please enter new sadran ID: ")
        age = int(input("Please enter new sadran age: "))
        phone_number =  input("Please enter new sadran phone number: ")
        employee_number =  input("Please enter new sadran employee number: ")
        vest_color =  input("Please enter new sadran vest color: ")
        new_sadran = Sadran(id, name, age, phone_number, employee_number, vest_color)
        FileHandler.add_worker(new_sadran)

    def add_cashier(self):
        from Models.Tools.FileHandler import FileHandler
        from Models.Entities.Cashier import Cashier
        name = input("Please enter new cashier name: ")
        id = input("Please enter new cashier ID: ")
        age = int(input("Please enter new cashier age: "))
        phone_number = input("Please enter new cashier phone number: ")
        employee_number = input("Please enter new cashier employee number: ")
        desk_number = int(input("Please enter new cashier desk number: "))
        new_cashier = Cashier(id, name, age, phone_number, employee_number, desk_number)
        FileHandler.add_worker(new_cashier)

    def remove_employee(self, employees: List[Employee]):
        from Models.Entities.Cashier import Cashier
        cashiers = []
        sadrans = []
        for employee in employees:
            if isinstance(employee, Sadran):
                sadrans.append(employee)
        for cashier in employees:
            if isinstance(cashier, Cashier):
                cashiers.append(cashier)

        employee_choose = int(input("-------------------------------\n"
                                    "Sadran or Cashier?:"
                                    "\n1. Sadran."
                                    "\n2. Cashier.\n"
                                    "-------------------------------\n-> "))

        if employee_choose == 1:
            for i in range(0, len(sadrans)):
                print(f"{i}. {sadrans[i].get_name()}")

            sadran_choose = int(input("Choose sadran to remove: "))
            sadrans.pop(sadran_choose)

            with open("../PythonFinal/Files/Employees/Sadran.txt", 'w') as file:
                for sadran in sadrans:
                    file.write(sadran.__str__())

        if employee_choose == 2:
            for i in range(0, len(cashiers)):
                print(f"{i}. {cashiers[i].get_name()}")

            cashier_choose = int(input("Choose cashier to remove: "))
            cashiers.pop(cashier_choose)

            with open("../PythonFinal/Files/Employees/Cashiers.txt", 'w') as file:
                for cashier in cashiers:
                    file.write(cashier.__str__())

    def sell_to_client(self, clients: List[Client]):
        from Models.Tools.Tools import Tools
        for i in range(0, len(clients)):
            print(Tools.client_purchase(f"           Client number {i+1}          "))
            clients[i].display_client()
            print("")

        chosen_client = int(input("Choose client number: "))-1
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
                FileHandler.append_products_to_file(f"../PythonFinal/Files/Clients/{client.get_id()}/existing_products.txt",
                                                    client, client.get_wishlist())
                FileHandler.add_purchase(new_purchase)
                return new_purchase



