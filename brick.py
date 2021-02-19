import global_var
import colorama
from colorama import Fore, Back, Style
colorama.init()

class Brick:
    def __init__(self):
        self.strength=1
        # self.x=x
        # self.y=y
    def abc(self):
        print(self.x)
    def render(self):
        if self.strength==0:
            color=' '
        elif self.strength==1:
            color='H'+Fore.WHITE
        elif self.strength==2:
            color='H'+Fore.YELLOW
        elif self.strength==3:
            color='H'+Fore.GREEN
        else:
            color='H'+Fore.RED
        for i in range(2):
            for j in range(5):
                global_var.display.grid[i+self.x][j+self.y]=color
    def clear(self):
        for i in range(2):
            for j in range(5):
                global_var.display.grid[i][j]=' '

class white_brick(Brick):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.strength=1

class yellow_brick(Brick):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.strength=2

class green_brick(Brick):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.strength=3

class unbreak_brick(Brick):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.strength=100