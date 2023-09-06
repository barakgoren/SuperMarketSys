class Product:
    def __init__(self, category: str, name: str, price: float):
        self._category: str = category
        self._name: str = name
        self._price: float = price

    def get_name(self):
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_cat(self):
        return self._category

    def __str__(self):
        return f"{self._category},{self._name},{self._price}"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self._name == other._name
        return False
