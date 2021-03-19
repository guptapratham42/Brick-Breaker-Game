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

levelarray=[]
levelarray.append([])
def initial_bricks():
    bricksarray=[]
    # bricksarray.append(brick.white_brick(5, 79))
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
    levelarray.append(bricksarray)
    bricksarray=[]
    for i in range(1, 6 ,4):
        for j in range(6, 90, 10):
            bricksarray.append(brick.white_brick(i, j))
    for i in range(3, 6 ,4):
        for j in range(11, 90, 10):
            bricksarray.append(brick.unbreak_brick(i, j))
    for i in range(1, 6 ,4):
        for j in range(11, 90, 10):
            bricksarray.append(brick.yellow_brick(i, j))
    for i in range(3, 6 ,4):
        for j in range(6, 90, 10):
            bricksarray.append(brick.green_brick(i, j))
    for j in range(36, 66, 5):
        bricksarray.append(brick.explosive_brick(7, j))
    levelarray.append(bricksarray)
    bricksarray=[]
    for i in range(21, 6 ,4):
        for j in range(6, 90, 10):
            bricksarray.append(brick.unbreak_brick(i, j))
    for i in range(3, 6 ,4):
        for j in range(11, 90, 10):
            bricksarray.append(brick.unbreak_brick(i, j))
    for i in range(1, 6 ,4):
        for j in range(11, 90, 10):
            bricksarray.append(brick.unbreak_brick(i, j))
    for i in range(3, 6 ,4):
        for j in range(6, 90, 10):
            bricksarray.append(brick.unbreak_brick(i, j))
    for j in range(36, 66, 5):
        bricksarray.append(brick.explosive_brick(7, j))
    levelarray.append(bricksarray)

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
leveltime=time.time()
if __name__ == "__main__":
    padd=paddle.paddle()
    ball=ball.Ball()
    initial_bricks()
    init_power()
    while (1):
        obj=abc.Get()
        inp=abc.input_to(obj)
        if inp == 'p':
            global_var.play*=-1
        if inp == 'l':
            global_var.level+=1
            leveltime=time.time()
            if global_var.level>=4:
                break
            global_var.paddle_mid=50
            global_var.paddle_start=47
            global_var.paddle_end=52
            global_var.paddle_length=25
            global_var.thru=1
            global_var.grab=1
            global_var.expolosion=0
            ball.__init__()
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
            for i in levelarray[global_var.level]:
                i.fall()
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
            # if(global_var.expolosion==1):
            for i in levelarray[global_var.level]:
                if global_var.expolosion==1 and i.expo==1:
                    for j in levelarray[global_var.level]:
                        if abs(j.x-i.x)<=2 and abs(i.y-j.y)<=5:
                            j.strength=0
                    # i.expo=0
            ball.updatevar()
            ball.ball_wall()
            if ball.ball_paddle() and time.time()-leveltime>=5:
                for i in levelarray[global_var.level]:
                    i.drop_brick()
            ball.lost()
            ball.render()
            global_var.pass_level=0
            for i in levelarray[global_var.level]:
                if i.strength>0:
                    global_var.pass_level=1
            if global_var.pass_level==0:
                global_var.level+=1
                leveltime=time.time()
                if global_var.level>=4:
                    break
                global_var.paddle_mid=50
                global_var.paddle_start=47
                global_var.paddle_end=52
                global_var.paddle_length=25
                global_var.thru=1
                global_var.grab=1
                global_var.expolosion=0
                ball.__init__()
            print("No of lives remaining: {}  Score: {}  Time played: {}".format(global_var.over, global_var.score, round(time.time()-starttime, 3)))
            if(global_var.over==0):
                break
            global_var.display.render()
            for i in poweruparray:
                i.clear()
            for i in range(global_var.height):
                for j in range(global_var.width):
                    global_var.display.grid[i][j]=' '+Back.BLACK + Fore.BLACK
    print("GAME OVER!")