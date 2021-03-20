#from global_var import *
import global_var
import colorama
import paddle
import os
from colorama import Fore, Back, Style
colorama.init()

class Bomb:
    def __init__(self):
        self.xpos=1
        self.ypos=global_var.paddle_mid
        self.xvel=1
        self.display=0
    def render(self):
        if self.display ==1:
            self.xpos+=self.xvel
            global_var.display.grid[self.xpos][self.ypos]=Fore.RED+'O'
    def bomb_go(self):
        self.display=1
        self.ypos=global_var.paddle_mid
    def clear(self):
        global_var.display.grid[self.xpos][self.ypos]=' '
    def ball_paddle(self):
        if self.xpos + self.xvel >= 28 and self.ypos>=global_var.paddle_start and self.ypos<=global_var.paddle_end and self.display==1:
            # self.xvel*=-1
            global_var.over-=1
            os.system('aplay -q ./losinglife.wav&')
            self.display=0
            # self.yvel+=int((self.ypos-global_var.paddle_mid)/2)
            # return True
    def lost(self):
        if self.xpos >=28 and self.display==1:
            # global_var.paddle_mid=50
            self.display=0