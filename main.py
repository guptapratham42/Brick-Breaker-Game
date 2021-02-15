import input as abc
import colorama
from colorama import Fore, Back, Style

if __name__ == "__main__":
    while (1):
        obj=abc.Get()
        inp=abc.input_to(obj)
        if inp=='q':
            break
        print(inp)