from typing import List
from Models.Entities.Employee import Employee
from Models.Interfaces.ILogistic import ILogistic
from Models.Inanimates.Shelf import Shelf
from Models.Inanimates.Product import Product


class Sadran(Employee, ILogistic):
    def __init__(self, id: str, name: str, age: int, phone_number:str, employee_number: str, vest_color: str):
        super().__init__(id, name, age, phone_number, employee_number)
        self._vest_color = vest_color

    def add_product(self, shelves: List[Shelf]):
        try:
            print("Choose shelf:")
            for i in range(0, len(shelves)):
                print(f"{(i+1)}. {shelves[i].get_name()}")
            print("-------------------------------\n> ")
            shelf_choose = int(input())-1

            shelf = shelves[shelf_choose]
            print("All existing products:")
            for i in range(0, len(shelf.get_product())):
                print(f"{i+1}. {shelf.get_product()[i].get_name()} (${shelf.get_product()[i].get_price()})")

            print("-------------------------------")
            print("Add product details:")
            new_product_category = input("Category: ")
            new_product_name = input("Name: ")
            try:
                new_product_price = float(input("Price: "))
            except BaseException:
                print("Must enter float")
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
        choosen_product_index = int(input("> "))-1
        choosen_product = shelf.get_product()[choosen_product_index]
        from Models.Tools.FileHandler import FileHandler
        FileHandler.remove_product_from_shelf(choosen_product, shelf)
        print("-------------------------------")
        print("Product removed!")

    def __str__(self):
        return f"{self._id},{self._name},{self._age},{self._phone_number},{self._employee_number},{self._vest_color}\n"
