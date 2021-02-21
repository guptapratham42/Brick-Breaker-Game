import global_var
import colorama
import ball
from colorama import Fore, Back, Style
colorama.init()

class Powerup:
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'E'
        self.x=x
        self.y=y
        self.display=0
    def render(self):
        if self.display==1:
            global_var.display.grid[self.x][self.y]=self.symbol
    def dropstart(self):
        self.display=1
    def magic(self):
        pass

class shrink(Powerup):
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'S'
        self.x=x
        self.y=y
        self.display=0

class multiply(Powerup):
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'M'
        self.x=x
        self.y=y
        self.display=0

class fast(Powerup):
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'F'
        self.x=x
        self.y=y
        self.display=0

class thru(Powerup):
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'T'
        self.x=x
        self.y=y
        self.display=0

class grab(Powerup):
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'G'
        self.x=x
        self.y=y
        self.display=0