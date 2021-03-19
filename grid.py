import colorama
from colorama import Fore, Back, Style
import numpy as np
import os
import sys
colorama.init()

class Grid:
    def __init__(self, height, width):
        self.height=height
        self.width=width
        self.grid=([[Back.BLACK + Fore.BLACK + " " for i in range(self.width)] for j in range(self.height)])
    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.grid[i][j], end="")
            print()
        #print(self.grid)
        sys.stdout.write("\033c")
    def clear(self):
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j] = ' '