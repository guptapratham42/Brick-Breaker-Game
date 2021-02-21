import input as abc
import colorama
from colorama import Fore, Back, Style
import grid as grid
import global_var
import paddle
import time
import ball
import brick
import powerup
import random

bricksarray=[]
def initial_bricks():
    for i in range(1, 6 ,4):
        for j in range(6, 90, 10):
            bricksarray.append(brick.white_brick(i, j))
    for i in range(3, 8 ,4):
        for j in range(11, 90, 10):
            bricksarray.append(brick.yellow_brick(i, j))
    for i in range(1, 6 ,4):
        for j in range(11, 90, 10):
            bricksarray.append(brick.unbreak_brick(i, j))
    for i in range(3, 8 ,4):
        for j in range(6, 90, 10):
            bricksarray.append(brick.green_brick(i, j))
    for j in range(36, 66, 5):
        bricksarray.append(brick.explosive_brick(9, j))

poweruparray=[]
def init_power():
    for i in range(2):
        x=2*random.randint(1, 4)-1
        y=5*random.randint(1, 17)+1
        poweruparray.append(powerup.Powerup(x, y))
    for i in range(2):
        x=2*random.randint(1, 4)-1
        y=5*random.randint(1, 17)+1
        poweruparray.append(powerup.shrink(x, y))
    for i in range(2):
        x=2*random.randint(1, 4)-1
        y=5*random.randint(1, 17)+1
        poweruparray.append(powerup.multiply(x, y))
    for i in range(2):
        x=2*random.randint(1, 4)-1
        y=5*random.randint(1, 17)+1
        poweruparray.append(powerup.fast(x, y))
    for i in range(2):
        x=2*random.randint(1, 4)-1
        y=5*random.randint(1, 17)+1
        poweruparray.append(powerup.thru(x, y))
    for i in range(2):
        x=2*random.randint(1, 4)-1
        y=5*random.randint(1, 17)+1
        poweruparray.append(powerup.grab(x, y))
# poweruparray.append(powerup.shrink(7, 66))
colorama.init()
starttime=time.time()
if __name__ == "__main__":
    padd=paddle.paddle()
    ball=ball.Ball()
    initial_bricks()
    init_power()
    # powe=powerup.Powerup(18, 50)
    while (1):
        # print(time.time())
        # print(xpower)
        obj=abc.Get()
        inp=abc.input_to(obj)
        if inp == 'p':
            global_var.play*=-1
        if inp=='q':
            break
        if inp==' ':
            global_var.grab=0
        if global_var.play==1:
            padd.clear()
            ball.clear()
            if inp != None:
                time.sleep(0.05)
            if inp=='d':
                padd.updatemid(2)
            if inp=='a':
                padd.updatemid(-2)
            padd.render()
            for i in bricksarray:
                i.render()
                i.brick_ball()
                for j in poweruparray:
                    if j.x==i.x and j.y==i.y and i.strength==0:
                        j.dropstart()
            for i in poweruparray:
                # i.dropstart()
                i.render()
                i.magichappen()
                i.killpower()
            if(global_var.expolosion==1):
                for i in bricksarray:
                    if i.x>=7 and i.y>=36 and i.y <=66:
                        i.strength=0
            ball.updatevar()
            ball.ball_wall()
            ball.ball_paddle()
            ball.lost()
            ball.render()
            # powe.dropstart()
            # powe.render()
            print("No of lives remaining: {}  Score: {}  Time played: {}".format(global_var.over, global_var.score, round(time.time()-starttime, 3)))
            # print(global_var.paddle_length)
            if(global_var.over==0):
                break
            global_var.display.render()
            for i in poweruparray:
                i.clear()
    print("GAME OVER!")