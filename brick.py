import global_var
import colorama
import ball
import random
from colorama import Fore, Back, Style
colorama.init()

class Brick:
    def __init__(self):
        self.strength=1
        self.expo=0
        # self.x=x
        # self.y=y
    def render(self):
        if self.strength<=0:
            color=' '+ Back.BLACK+ Fore.BLACK
        elif self.strength==1 and self.expo==1:
            color='H'+ Back.BLACK+Fore.CYAN
        elif self.strength==1:
            color='H'+Back.BLACK+Fore.WHITE
        elif self.strength==2:
            color='H'+ Back.BLACK+Fore.YELLOW
        elif self.strength==3:
            color='H'+ Back.BLACK+Fore.GREEN
        else:
            color='H'+ Back.BLACK+Fore.RED
        for i in range(2):
            for j in range(5):
                global_var.display.grid[i+self.x][j+self.y]=color
    def clear(self):
        for i in range(2):
            for j in range(5):
                global_var.display.grid[i][j]=' '
    def drop_brick(self):
        self.x+=1
    def fall(self):
        if self.x+2>=global_var.height-1:
            global_var.over=0
            # global_var.level=
    def brick_ball(self):
        if(self.strength>0):
            # Lower side collision handle
            low_col=global_var.ball_vely/global_var.ball_velx
            low_col*=(self.x+1-global_var.ball_x)
            low_col+=global_var.ball_y
            if (((low_col)>=self.y) and ((low_col)<=self.y+4) and (self.x+1<=global_var.ball_x) and (self.x+1>=global_var.ball_x+global_var.ball_velx)):
                if (global_var.thru!=0):
                    global_var.ball_velx*=-1
                self.strength-=1
                self.contact=1
                global_var.score+=10

            # upper side collision handle
            upp_col=global_var.ball_vely/global_var.ball_velx
            upp_col*=(self.x-global_var.ball_x)
            upp_col+=global_var.ball_y 
            if (((upp_col)>=self.y) and ((upp_col)<=self.y+4) and (self.x>=global_var.ball_x) and (self.x<=global_var.ball_x+global_var.ball_velx)):
                if(global_var.thru!=0):
                    global_var.ball_velx*=-1
                self.strength-=1
                self.contact=1
                global_var.score+=10

            # left side collision handle
            if global_var.ball_vely!=0:
                lef_col=global_var.ball_velx/global_var.ball_vely
                lef_col*=(self.y-global_var.ball_y)
                lef_col+=global_var.ball_x
                if (((lef_col)>=self.x) and ((lef_col)<=self.x+1) and (self.y>=global_var.ball_y) and (self.y<=global_var.ball_y+global_var.ball_vely)):
                    if(global_var.thru!=0):
                        global_var.ball_vely*=-1
                    self.strength-=1
                    self.contact=1
                    global_var.score+=10

            # right side collision handle
            if global_var.ball_vely!=0:
                rig_col=global_var.ball_velx/global_var.ball_vely
                rig_col*=(self.y+4-global_var.ball_y)
                rig_col+=global_var.ball_x
                if (((rig_col)>=self.x) and ((rig_col)<=self.x+1) and (self.y+4<=global_var.ball_y) and (self.y+4>=global_var.ball_y+global_var.ball_vely)):
                    if(global_var.thru!=0):
                        global_var.ball_vely*=-1
                    self.strength-=1
                    self.contact=1
                    global_var.score+=10
            
            #updation
            a=ball.Ball()
            a.updatevar()
            if (self.strength==0 and self.expo==1):
                global_var.expolosion=1
    def rainbow_contact(self):
        if self.rainbow == 1 and self.contact==0:
            self.strength=random.randint(1, 3)


class white_brick(Brick):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.contact=0
        self.rainbow=0
        self.expo=0
        self.strength=1

class yellow_brick(Brick):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.contact=0
        self.rainbow=0
        self.expo=0
        self.strength=2

class green_brick(Brick):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.contact=0
        self.rainbow=0
        self.expo=0
        self.strength=3

class unbreak_brick(Brick):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.contact=0
        self.rainbow=0
        self.expo=0
        self.strength=1000

class explosive_brick(Brick):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.contact=0
        self.rainbow=0
        self.strength=1
        self.expo=1

class rainbow_brick(Brick):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.contact=0
        self.expo=0
        self.strength=1
        self.rainbow=1