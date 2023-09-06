from typing import List, TYPE_CHECKING
from Models.Inanimates.Shelf import Shelf
from Models.Inanimates.Product import Product
from Models.Inanimates.Purchase import Purchase
from Models.Inanimates.PurchaseDisplay import PurchaseDisplay
from Models.Entities.Client import Client
from Models.Entities.Sadran import Sadran
from Models.Entities.ShiftManager import ShiftManager
from Models.Entities.SuperManager import SuperManager
from Models.Entities.Cashier import Cashier
from Models.Entities.Employee import Employee
from Models.Tools.Tools import Tools
import os
import subprocess


class FileHandler:

    @staticmethod
    def say(text):
        subprocess.call(['say', text])


    @staticmethod
    def read_shelves_from_directory(directory_path: str) -> List[Shelf]:
        shelves = []
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                shelf_name = os.path.splitext(filename)[0]
                products = []
                with open(file_path, 'r') as file:
                    for line in file:
                        product_data = line.strip().split(',')
                        category = product_data[0].strip()
                        name = product_data[1].strip()
                        price = float(product_data[2])
                        product = Product(category, name, price)
                        products.append(product)

                shelf = Shelf(shelf_name, products)
                shelves.append(shelf)

        return shelves

    @staticmethod
    def read_clients(directory_path: str) -> List[Client]:
        clients = []
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            id = os.path.basename(file_path)
            wanted_products = []
            existing_products = []
            with open(f"{file_path}/details.txt", 'r') as file:
                name = file.readline().strip()
                age = int(file.readline())
                phone_number = file.readline().strip()

            with open(f"{file_path}/wanted_products.txt", 'r') as file:
                line = file.readline()
                while line:
                    product_att = line.strip().split(',')
                    prod_cat = product_att[0].strip()
                    prod_name = product_att[1].strip()
                    prod_price = float(product_att[2])
                    cur_product = Product(prod_cat, prod_name, prod_price)
                    wanted_products.append(cur_product)

                    line = file.readline()
                    if not line:
                        break

            with open(f"{file_path}/existing_products.txt", 'r') as file:
                line = file.readline()
                while line:
                    product_att = line.strip().split(',')
                    prod_cat = product_att[0].strip()
                    prod_name = product_att[1].strip()
                    prod_price = float(product_att[2])
                    cur_product = Product(prod_cat, prod_name, prod_price)
                    existing_products.append(cur_product)
                    line = file.readline()
                    if not line:
                        break

            client = Client(id, name, age, phone_number, wanted_products, existing_products)
            clients.append(client)

        return clients

    @staticmethod
    def read_employees_from_directory(directory_path: str) -> List[Employee]:
        employees = []

        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            employee_type = os.path.splitext(filename)[0]
            if os.path.isfile(file_path):

                if employee_type == 'Cashiers':
                    employees.extend(FileHandler.read_cashiers_from_file(file_path))
                elif employee_type == 'Sadran':
                    employees.extend(FileHandler.read_sadrans_from_file(file_path))
                elif employee_type == 'SuperManagers':
                    employees.extend(FileHandler.read_super_managers_from_file(file_path))

        return employees

    @staticmethod
    def read_cashiers_from_file(file_path: str) -> List[Cashier]:
        cashiers = []
        with open(file_path, 'r') as file:
            for line in file:
                # Parse cashier details from the line
                id, name, age, phone_number, employee_number, desk_number = line.strip().split(',')

                # Create a Cashier object and add it to the list
                cashier = Cashier(id, name, int(age), phone_number, employee_number, int(desk_number))
                cashiers.append(cashier)

        return cashiers

    @staticmethod
    def read_sadrans_from_file(file_path: str) -> List[Sadran]:
        sadrans = []

        with open(file_path, 'r') as file:
            for line in file:
                # Parse sadran details from the line
                id, name, age, phone_number, employee_number, vest_color = line.strip().split(',')

                # Create a Sadran object and add it to the list
                sadran = Sadran(id, name, int(age), phone_number, employee_number, vest_color)
                sadrans.append(sadran)

        return sadrans

    @staticmethod
    def read_shift_managers_from_directory(directory_path: str) -> List[ShiftManager]:
        shift_managers = []
        workers = []
        for dir_name in os.listdir(directory_path):
            id = dir_name
            with open(f"{directory_path}/{dir_name}/details.txt", 'r') as file:
                name = file.readline().strip()
                age = int(file.readline())
                phone_number = file.readline().strip()
                employee_number = file.readline().strip()
                hourly_salary = float(file.readline())

            with open(f"{directory_path}/{dir_name}/workers.txt", 'r') as file:
                for id in file:
                    if not id:
                        break
                    employee_id = id.strip()
                    existing_employees = FileHandler.read_employees_from_directory("../PythonFinal/Files/Employees")
                    for employee in existing_employees:
                        if employee.get_id() == employee_id:
                            workers.append(employee)

            shift_managers.append(ShiftManager(id, name, age, phone_number, employee_number, workers, hourly_salary))
            workers.clear()

        return shift_managers

    @staticmethod
    def read_super_managers_from_file(file_path: str) -> List[SuperManager]:
        super_managers = []

        with open(file_path, 'r') as file:
            for line in file:
                # Parse super manager details from the line
                id, name, age, phone_number, employee_number, manager_code = line.strip().split('^')

                # Create a SuperManager object and add it to the list
                super_manager = SuperManager(id, name, int(age), phone_number, employee_number, manager_code)
                super_managers.append(super_manager)

        return super_managers

    @staticmethod
    def append_products_to_file(file_path: str, client: Client, products: List[Product]):
        with open(file_path, 'a') as file:
            for product in products:
                if product not in client.get_existing_products():
                    line = f"{product.get_cat()},{product.get_name()},{product.get_price()}\n"
                    file.write(line)

        with open(f"../PythonFinal/Files/Clients/{client.get_id()}/wanted_products.txt", 'w'):
            pass

        client.set_wishlist([])

    @staticmethod
    def add_to_wishlist_file(file_path: str, client: Client, product: Product):
        with open(file_path, 'a') as file:
            if product not in client.get_wishlist():
                line = f"{product.get_cat()},{product.get_name()},{product.get_price()}\n"
                file.write(line)

    @staticmethod
    def add_product_to_shelf(product: Product, shelf: Shelf):
        file_path = f"../PythonFinal/Files/Shelves/{shelf.get_name()}.txt"
        with open(file_path, 'a') as file:
            file.write(product.__str__())

    @staticmethod
    def remove_product_from_shelf(product: Product, shelf: Shelf):
        products_list = shelf.get_product()
        for i in range(0, len(products_list)):
            if products_list[i].__eq__(product):
                products_list.pop(i)
                break

        file_path = f"../PythonFinal/Files/Shelves/{shelf.get_name()}.txt"
        with open(file_path, 'w') as file:
            for product in products_list:
                file.write(product.__str__()+"\n")

    @staticmethod
    def add_purchase(purchase: Purchase):
        try:
            os.makedirs(f"../PythonFinal/Files/Purchases/{Tools.get_current_date()}")
            os.makedirs(f"../PythonFinal/Files/Purchases/{Tools.get_current_date()}/{Tools.get_current_hour()}")
        except FileExistsError:
            os.makedirs(f"../PythonFinal/Files/Purchases/{Tools.get_current_date()}/{Tools.get_current_hour()}")

        with open(f"../PythonFinal/Files/Purchases/{Tools.get_current_date()}/{Tools.get_current_hour()}/details.txt",
                  'a') as file:
            file.write(purchase.__str__())

        with open(f"../PythonFinal/Files/Purchases/{Tools.get_current_date()}/{Tools.get_current_hour()}/products.txt",
                  'a') as file:
            for product in purchase.get_products():
                file.write(f"{product.get_cat()}^{product.get_name()}^{product.get_price()}\n")

    @staticmethod
    def read_purchases():
        today_directory = f"../PythonFinal/Files/Purchases/{Tools.get_current_date()}"
        purchases = []
        try:
            for dir_name in os.listdir(today_directory):
                inside_purchase = os.path.join(today_directory, dir_name)

                with open(f"{inside_purchase}/details.txt", 'r') as file:
                    attributes = file.readline().split("^")
                    date = dir_name
                    buyer_name = attributes[1]
                    cashier_name = attributes[2]
                    total_price = float(attributes[3])

                products = []
                with open(f"{inside_purchase}/products.txt") as file:
                    line = file.readline()
                    while line:
                        product_cat = line.split("^")[0]
                        product_name = line.split("^")[1]
                        product_price = float(line.split("^")[2])
                        new_product = Product(product_cat, product_name, product_price)
                        products.append(new_product)
                        line = file.readline()

                new_purchase = PurchaseDisplay(date, buyer_name, cashier_name, total_price, products)
                purchases.append(new_purchase)
        except FileNotFoundError:
            return purchases

        return purchases

    @staticmethod
    def add_worker(employee: Employee):

        if isinstance(employee, ShiftManager):
            dir_path = f"../PythonFinal/Files/Employees/ShiftManagers/{employee.get_id()}"
            os.mkdir(dir_path)
            with open(f"{dir_path}/details.txt", 'w') as file:
                file.write(employee.get_name() + "\n")
                file.write(str(employee.get_age()) + "\n")
                file.write(employee.get_phone() + "\n")
                file.write(employee.get_employee_number() + "\n")
                file.write(str(employee.get_salary()))

            with open(f"{dir_path}/workers.txt", 'w') as file:
                for worker in employee.get_workers():
                    file.write(worker.get_id() + "\n")


        else:
            if isinstance(employee, Sadran):
                file_path = "../PythonFinal/Files/Employees/Sadran.txt"

            if isinstance(employee, Cashier):
                file_path = "../PythonFinal/Files/Employees/Cashiers.txt"

            with open(file_path, 'a') as file:
                file.write(employee.__str__())
