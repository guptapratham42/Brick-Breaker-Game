import global_var
import colorama
import ball
import time
import numpy
import math
from colorama import Fore, Back, Style
colorama.init()

class Powerup:
    def __init__(self, x, y):
        self.symbol=Fore.WHITE+'E'
        self.x=x
        self.y=y
        self.display=0
        self.magic=0
        self.timestart=0
        self.xvel=1
        self.yvel=0
        self.xacc=1
    def render(self):
        if self.display==1:
            global_var.display.grid[self.x][self.y]=self.symbol
            if(self.xvel%3==1):
                self.xvel+=self.xacc
            self.y+=self.yvel
            # self.xvel=math.floor(self.xvel)
            self.x+=self.xvel
        if self.x+self.xvel>=28:
            if self.y+self.yvel>=global_var.paddle_start and self.y+self.yvel<=global_var.paddle_end:
                self.magic=1
                self.timestart=time.time()
            global_var.display.grid[self.x-1][self.y]=' '
            self.display=0
            self.x=0
            self.y=0
        if time.time()-self.timestart>10:
            self.magic=0
    def dropstart(self):
        self.xvel=global_var.ball_velx
        self.yvel=global_var.ball_vely
        self.display=1
    def drop_with_brick(self):
        self.x+=1
    def magichappen(self):
        if global_var.paddle_end<global_var.width-2 and global_var.paddle_start>=1 and self.magic==1:
            global_var.paddle_length+=2
            global_var.paddle_end+=1
            global_var.paddle_start-=1
            self.magic=0
    def killpower(self):
        if (time.time()-self.timestart>10 and self.timestart>0):
            self.timestart=0
            global_var.paddle_length-=2
            global_var.paddle_end-=1
            global_var.paddle_start+=1
    def clear(self):
        global_var.display.grid[self.x-1][self.y]=' '
    def powerup_wall(self):
        if self.y + self.yvel >= global_var.width or self.y + self.yvel <= 0:
            self.yvel*=-1
        if self.x + self.xvel<0:
            self.xvel*=-1

class shrink(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol=Fore.WHITE+'S'
        self.display=0
        self.magic=0
        self.timestart=0
    def magichappen(self):
        if global_var.paddle_length>2 and self.magic==1:
            global_var.paddle_length-=2
            global_var.paddle_end-=1
            global_var.paddle_start+=1
            self.magic=0
    def killpower(self):
        if (time.time()-self.timestart>10 and self.timestart>0):
            self.timestart=0
            global_var.paddle_length+=2
            global_var.paddle_end+=1
            global_var.paddle_start-=1

class multiply(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol=Fore.WHITE+'M'
        self.display=0
        self.magic=0
        self.timestart=0
    def killpower(self):
        pass

class fast(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol=Fore.WHITE+'F'
        self.display=0
        self.magic=0
        self.timestart=0
    def magichappen(self):
        if self.magic==1:
            global_var.ball_vely=global_var.ball_vely+2
            a=ball.Ball()
            a.updatevar()
            self.magic=0
    def killpower(self):
        if (time.time()-self.timestart>10 and self.timestart>0):
            self.timestart=0
            global_var.ball_vely=global_var.ball_vely-2
            a=ball.Ball()
            a.updatevar()

class thru(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol=Fore.WHITE+'T'
        self.display=0
        self.magic=0
        self.timestart=0
    def magichappen(self):
        if self.magic==1:
            global_var.thru=0
            self.magic=0
    def killpower(self):
        if (time.time()-self.timestart>10 and self.timestart>0):
            self.timestart=0
            global_var.thru=1

class grab(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.symbol=Fore.WHITE+'G'
        self.display=0
        self.magic=0
        self.timestart=0
    def magichappen(self):
        if self.magic==1:
            global_var.grab=1
            self.magic=0
    def killpower(self):
        if (time.time()-self.timestart>10 and self.timestart>0):
            self.timestart=0
            global_var.grab=0