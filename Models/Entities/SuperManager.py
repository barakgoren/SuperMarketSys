from Models.Entities.Employee import Employee
from Models.Inanimates.Shelf import Shelf
from typing import List


class SuperManager(Employee):
    def __init__(self, id: str, name: str, age: int, phone_number: str, employee_number: str, manager_code: str):
        super().__init__(id, name, age, phone_number, employee_number)
        self._manager_code: str = manager_code


    def display_shelves(self, shelves: List[Shelf]):
        for shelf in shelves:
            shelf.display_shelf()

    def add_shift_manager(self, employees: List[Employee]):
        from Models.Tools.FileHandler import FileHandler
        from Models.Entities.ShiftManager import ShiftManager
        from Models.Entities.Sadran import Sadran
        from Models.Entities.Cashier import Cashier
        from Models.Tools.Tools import Tools
        name = input("Please enter new shift manager name: ")
        id = input("Please enter new shift manager ID: ")
        age = int(input("Please enter new shift manager age: "))
        phone_number = input("Please enter new shift manager phone number: ")
        employee_number = input("Please enter new shift manager employee number: ")
        hourly_salary = float(input("Please enter new shift manager hourly salary: "))
        # ------------ just building a list of workers for the shift manager ------------
        workers: List[Employee] = []
        cashiers = [employee for employee in employees if isinstance(employee, Cashier)]
        sadranim = [employee for employee in employees if isinstance(employee, Sadran)]
        no_managers = []
        no_managers.extend(cashiers)
        no_managers.extend(sadranim)
        chosen_employee = 0
        for i in range(0, len(no_managers)):
            if not isinstance(no_managers[i], ShiftManager) and not isinstance(no_managers[i], SuperManager):
                print(Tools.shiftmanager_background(f"          Employee number {i + 1}"))
                no_managers[i].display_employee()
        while True:
            try:
                chosen_employee = int(input("Choose Employee: ")) - 1
                workers.append(no_managers[chosen_employee])
            except BaseException:
                print("done picking")
                break
        # ------------ just building a list of workers for the shift manager ------------

        new_shift_manager = ShiftManager(id, name, age, phone_number, employee_number, workers, hourly_salary)
        FileHandler.add_worker(new_shift_manager)

    def add_sadran(self):
        from Models.Tools.FileHandler import FileHandler
        from Models.Entities.Sadran import Sadran
        name = input("Please enter new sadran name: ")
        id = input("Please enter new sadran ID: ")
        age = int(input("Please enter new sadran age: "))
        phone_number = input("Please enter new sadran phone number: ")
        employee_number = input("Please enter new sadran employee number: ")
        vest_color = input("Please enter new sadran vest color: ")
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
        from Models.Entities.Sadran import Sadran
        from Models.Tools.Tools import Tools
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
                print(Tools.shiftmanager_background(f"          Sadran number {i+1}"))
                sadrans[i].display_employee()

            sadran_choose = int(input("Choose sadran to remove: "))-1
            sadrans.pop(sadran_choose)

            with open("../PythonFinal/Files/Employees/Sadran.txt", 'w') as file:
                for sadran in sadrans:
                    file.write(sadran.__str__())

        if employee_choose == 2:
            for i in range(0, len(cashiers)):
                print(Tools.shiftmanager_background(f"          Sadran number {i + 1}"))
                cashiers[i].display_employee()

            cashier_choose = int(input("Choose cashier to remove: "))
            cashiers.pop(cashier_choose)

            with open("../PythonFinal/Files/Employees/Cashiers.txt", 'w') as file:
                for cashier in cashiers:
                    file.write(cashier.__str__())
