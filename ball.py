#from global_var import *
import global_var
import colorama
from colorama import Fore, Back, Style
colorama.init()

class Ball:
    def __init__(self):
        self.xpos=27
        self.ypos=50
        self.xvel=-1
        self.yvel=1
    def render(self):
        self.xpos+=self.xvel
        self.ypos+=self.yvel
        global_var.display.grid[self.xpos][self.ypos]=Fore.RED+'@'
    def clear(self):
        global_var.display.grid[self.xpos][self.ypos]=' '
    def ball_wall(self):
        if self.ypos + self.yvel >= global_var.width or self.ypos + self.yvel <= 0:
            self.yvel*=-1
        if self.xpos + self.xvel<=0:
            self.xvel*=-1
    def ball_paddle(self):
        if self.xpos + self.xvel >= 28 and self.ypos>=global_var.paddle_start and self.ypos<=global_var.paddle_end:
            self.xvel*=-1
            self.yvel+=self.ypos-global_var.paddle_mid
    def lost(self):
        if self.xpos >=29:
            global_var.over=1