from abc import ABC
from Models.Entities.Person import Person


class Employee(Person, ABC):
    def __init__(self, id: str, name: str, age: int, phone_number: str, employee_number: str):
        super().__init__(id, name, age, phone_number)
        self._employee_number: str = employee_number

    def get_employee_number(self):
        return self._employee_number

    def display_employee(self):
        from Models.Entities.Sadran import Sadran
        from Models.Entities.Cashier import Cashier
        from Models.Entities.ShiftManager import ShiftManager
        from Models.Tools.Tools import Tools
        if isinstance(self, Sadran):
            print(Tools.sadran_background("                 Sadran"))
            print(Tools.sadran_background(f"Sadran Name: {self._name}"))
            print(Tools.sadran_background(f"Sadran ID: {self._id}"))
            print(Tools.sadran_background(f"Sadran Phone Number: {self._phone_number}"))
            print(Tools.sadran_background(f"Sadran Vest Color: {self._vest_color}"))
            print()
        if isinstance(self, Cashier):
            print(Tools.cashier_background("                 Cashier"))
            print(Tools.cashier_background(f"Cashier Name: {self._name}"))
            print(Tools.cashier_background(f"Cashier ID: {self._id}"))
            print(Tools.cashier_background(f"Cashier Phone Number: {self._phone_number}"))
            print(Tools.cashier_background(f"Cashier Desk Number: {self._desk_number}"))
            print()
        if isinstance(self, ShiftManager):
            print(Tools.shiftmanager_background("            Shift Manager"))
            print(Tools.shiftmanager_background(f"Shift Manager Name: {self._name}"))
            print(Tools.shiftmanager_background(f"Shift Manager ID: {self._id}"))
            print(Tools.shiftmanager_background(f"Shift Manager Phone Number: {self._phone_number}"))
            print()
        from Models.Entities.SuperManager import SuperManager
        if isinstance(self, SuperManager):
            print(Tools.supermanager_background("            Super Manager"))
            print(Tools.supermanager_background(f"Super Manager Name: {self._name}"))
            print(Tools.supermanager_background(f"Super Manager ID: {self._id}"))
            print(Tools.supermanager_background(f"Super Manager Phone Number: {self._phone_number}"))
            print(Tools.supermanager_background(f"Super Manager Code: *************"))
            print()

    def str(self):
        pass

    def eql(self):
        pass
