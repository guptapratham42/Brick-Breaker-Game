#from global_var import *
import global_var
import colorama
import paddle
import os
from colorama import Fore, Back, Style
colorama.init()

class Ball:
    def __init__(self):
        self.xpos=27
        self.ypos=50
        self.xvel=-1
        self.yvel=1
    def render(self):
        # print(self.xvel)
        if self.ypos + self.yvel >= global_var.width or self.ypos + self.yvel <= 0:
            self.yvel*=-1
        if self.xpos + self.xvel<0:
            self.xvel*=-1
        if global_var.grab==1 and self.xpos>=27:
            self.ypos=global_var.paddle_mid
        else:
            self.xpos+=self.xvel
            self.ypos+=self.yvel
        global_var.display.grid[self.xpos][self.ypos]=Fore.YELLOW+'@'
        global_var.ball_velx=self.xvel
        global_var.ball_vely=self.yvel
        global_var.ball_x=self.xpos
        global_var.ball_y=self.ypos
    def clear(self):
        global_var.display.grid[self.xpos][self.ypos]=' '
    def ball_wall(self):
        if self.ypos + self.yvel >= global_var.width or self.ypos + self.yvel <= 0:
            self.yvel*=-1
            os.system('aplay -q ./wall.wav&')
        if self.xpos + self.xvel<0:
            self.xvel*=-1
            os.system('aplay -q ./wall.wav&')
    def ball_paddle(self):
        if self.xpos + self.xvel >= 28 and self.ypos>=global_var.paddle_start and self.ypos<=global_var.paddle_end:
            self.xvel*=-1
            self.yvel+=int((self.ypos-global_var.paddle_mid)/2)
            # os.system('aplay -q ./sound1.wav&')
            return True
    def lost(self):
        if self.xpos >=28:
            global_var.over-=1
            os.system('aplay -q ./losinglife.wav&')
            self.xpos=27
            self.ypos=50
            self.xvel=-1
            self.yvel=1
            global_var.paddle_mid=50
            a=paddle.paddle()
            # a.updatemid(0)
            # global_var.play=-1
            global_var.grab=1
            # a.clear()
            # a.render()
    def updatevar(self):
        # self.ypos=global_var.ball_y
        # self.xpos=global_var.ball_x
        # print(self.xvel)
        self.xvel=global_var.ball_velx
        self.yvel=global_var.ball_vely
        # print(self.xvel)