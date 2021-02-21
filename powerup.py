import global_var
import colorama
import ball
import time
import numpy
from colorama import Fore, Back, Style
colorama.init()

class Powerup:
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'E'
        self.x=x
        self.y=y
        self.display=0
        self.magic=0
        self.timestart=99999999
    def render(self):
        if self.display==1:
            global_var.display.grid[self.x][self.y]=self.symbol
            self.x+=1
        if self.x>=28:
            if self.y>=global_var.paddle_start and self.y<=global_var.paddle_end:
                self.magic=1
                self.timestart=time.time()
            global_var.display.grid[self.x-1][self.y]=' '
            self.display=0
            self.x=0
        if time.time()-self.timestart>10:
            self.magic=0
    def dropstart(self):
        self.display=1
    def magichappen(self):
        if global_var.paddle_end<global_var.width-2 and global_var.paddle_start>=1 and self.magic==1:
            global_var.paddle_length+=2
            global_var.paddle_end+=1
            global_var.paddle_start-=1
            self.magic=0
    def killpower(self):
        if time.time()-self.timestart>10:
            global_var.paddle_length-=2
            global_var.paddle_end-=1
            global_var.paddle_start+=1
    def clear(self):
        global_var.display.grid[self.x-1][self.y]=' '

class shrink(Powerup):
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'S'
        self.x=x
        self.y=y
        self.display=0
        self.magic=0
        self.timestart=99999999
    def magichappen(self):
        if global_var.paddle_length>2 and self.magic==1:
            global_var.paddle_length-=2
            global_var.paddle_end-=1
            global_var.paddle_start+=1
            self.magic=0
    def killpower(self):
        if time.time()-self.timestart>10:
            global_var.paddle_length+=2
            global_var.paddle_end+=1
            global_var.paddle_start-=1

class multiply(Powerup):
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'M'
        self.x=x
        self.y=y
        self.display=0
        self.magic=0
        self.timestart=99999999
    def killpower(self):
        pass

class fast(Powerup):
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'F'
        self.x=x
        self.y=y
        self.display=0
        self.magic=0
        self.timestart=99999999
    def magichappen(self):
        if self.magic==1:
            global_var.ball_vely=global_var.ball_vely+2
            a=ball.Ball()
            a.updatevar()
            self.magic=0
    def killpower(self):
        if time.time()-self.timestart>10:
            global_var.ball_vely=global_var.ball_vely-2
            a=ball.Ball()
            a.updatevar()

class thru(Powerup):
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'T'
        self.x=x
        self.y=y
        self.display=0
        self.magic=0
        self.timestart=99999999
    def magichappen(self):
        if self.magic==1:
            global_var.thru=0
            self.magic=0
    def killpower(self):
        if time.time()-self.timestart>10:
            global_var.thru=1

class grab(Powerup):
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'G'
        self.x=x
        self.y=y
        self.display=0
        self.magic=0
        self.timestart=99999999
    def magichappen(self):
        if self.magic==1:
            global_var.grab=1
            self.magic=0
    def killpower(self):
        if time.time()-self.timestart>10:
            global_var.grab=0