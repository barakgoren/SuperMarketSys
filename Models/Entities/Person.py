from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, id: str, name: str, age: int, phone_number:str):
        self._id: str = id
        self._name: str = name
        self._age: int = age
        self._phone_number: str = phone_number

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_phone(self):
        return self._phone_number

    def get_age(self):
        return self._age

    @abstractmethod
    def str(self):
        pass

    @abstractmethod
    def eql(self):
        pass
