from abc import ABC, abstractmethod
from typing import List
from Models.Inanimates.Shelf import Shelf
from Models.Inanimates.Product import Product


class ILogistic(ABC):

    @abstractmethod
    def add_product(self, shelves: List[Shelf]):
        pass

    @abstractmethod
    def remove_product(self, shelves: List[Shelf]):
        pass
