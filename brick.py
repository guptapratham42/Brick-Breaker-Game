import global_var
import colorama
from colorama import Fore, Back, Style
colorama.init()

class Brick:
    def __init__(self):
        self.strength=10
    def abc(self):
        print(self.strength)
    def render(self):
        for i in range(2):
            for j in range(5):
                global_var.display.grid[i][j]='H'
    def clear(self):
        for i in range(2):
            for j in range(5):
                global_var.display.grid[i][j]=' '
class white_brick(Brick):
    def __init__(self):
        self.strength=1
        # super().__init__()