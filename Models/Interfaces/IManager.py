from abc import abstractmethod, ABC
from Models.Entities.Employee import Employee


class IManager(ABC):

    @abstractmethod
    def add_employee(self, employee: Employee):
        pass

    @abstractmethod
    def remove_employee(self):
        pass


