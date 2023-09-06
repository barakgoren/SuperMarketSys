from Models.Inanimates.Supermarket import Supermarket
from colorama import init, Fore, Back, Style


if __name__ == '__main__':
    init()
    while True:
        rami_levi = Supermarket()
        rami_levi.start()
