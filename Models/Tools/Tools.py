from datetime import datetime, timezone
from Models.Inanimates.Product import Product
import pytz
from colorama import init, Fore, Back, Style


class Tools:
    api_key = ''

    @staticmethod
    def add_spaces(num):
        spaces = ""
        for item in range(0, num):
            spaces += " "
        return spaces

    @staticmethod
    def paint_shiftmanager(text):
        return f"{Fore.LIGHTCYAN_EX}{text}{Style.RESET_ALL}"

    @staticmethod
    def paint_super_manager(text):
        return f"{Fore.LIGHTMAGENTA_EX}{text}{Style.RESET_ALL}"

    @staticmethod
    def paint_sadran(text):
        return f"{Fore.GREEN}{text}{Style.RESET_ALL}"

    @staticmethod
    def paint_cashier(text):
        return f"{Fore.RED}{text}{Style.RESET_ALL}"

    @staticmethod
    def paint_client(text):
        return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"

    @staticmethod
    def print_products(product: Product, reduce: int):
        delta = 39
        price_as_str = str(product.get_price())
        digits = len(price_as_str)
        name = product.get_name()
        spaces = Tools.add_spaces(delta - digits - len(name) - reduce)
        price = product.get_price()
        return f"{Fore.BLACK + Back.RED}{name}{spaces}${product.get_price()}{Style.RESET_ALL}"

    @staticmethod
    def red_background(text):
        return f"{Fore.BLACK + Back.RED}{text}{Style.RESET_ALL}"


    @staticmethod
    def sadran_background(text):
        text_delta = 42 - len(text)
        if text_delta > 0:
            text += Tools.add_spaces(text_delta)
        return f"{Fore.BLACK + Back.GREEN}{text}{Style.RESET_ALL}"

    @staticmethod
    def cashier_background(text):
        text_delta = 42 - len(text)
        if text_delta > 0:
            text += Tools.add_spaces(text_delta)
        return f"{Fore.BLACK + Back.RED}{text}{Style.RESET_ALL}"

    @staticmethod
    def shiftmanager_background(text):
        text_delta = 42 - len(text)
        if text_delta > 0:
            text += Tools.add_spaces(text_delta)
        return f"{Fore.BLACK + Back.LIGHTCYAN_EX}{text}{Style.RESET_ALL}"

    @staticmethod
    def supermanager_background(text):
        text_delta = 42 - len(text)
        if text_delta > 0:
            text += Tools.add_spaces(text_delta)
        return f"{Fore.BLACK + Back.LIGHTMAGENTA_EX}{text}{Style.RESET_ALL}"

    @staticmethod
    def client_background(text):
        text_delta = 42 - len(text)
        if text_delta > 0:
            text += Tools.add_spaces(text_delta)
        return f"{Fore.BLACK + Back.YELLOW}{text}{Style.RESET_ALL}"

    @staticmethod
    def purchase_background(text):
        text_delta = 31 - len(text)
        if text_delta > 0:
            text += Tools.add_spaces(text_delta)
        return f"{Fore.BLACK + Back.BLUE}{text}{Style.RESET_ALL}"

    @staticmethod
    def purchase_background_total(product: Product, reduce):
        delta = 28
        price_as_str = str(product.get_price())
        digits = len(price_as_str)
        name = product.get_name()
        spaces = Tools.add_spaces(delta - digits - len(name) - reduce)
        price = product.get_price()
        return f"{Fore.BLACK + Back.BLUE}- {name}{spaces}${product.get_price()}{Style.RESET_ALL}"

    @staticmethod
    def client_purchase(text):
        text_delta = 42 - len(text)
        if text_delta > 0:
            text += Tools.add_spaces(text_delta)
        return f"{Fore.BLACK + Back.LIGHTBLUE_EX}{text}{Style.RESET_ALL}"

    @staticmethod
    def get_current_time():
        return datetime.now(pytz.timezone("Asia/Jerusalem")).strftime("%d/%m/%y - %H:%M:%S")

    @staticmethod
    def get_current_date():
        return datetime.now(pytz.timezone("Asia/Jerusalem")).strftime("%d-%m-%y")

    @staticmethod
    def get_current_hour():
        return datetime.now(pytz.timezone("Asia/Jerusalem")).strftime("%H:%M:%S")
