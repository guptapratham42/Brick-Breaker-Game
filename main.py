import input as abc
import colorama
from colorama import Fore, Back, Style
import grid as grid
import global_var
import paddle
import time
import ball
import brick

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
colorama.init()
if __name__ == "__main__":
    padd=paddle.paddle()
    ball=ball.Ball()
    initial_bricks()
    while (1):
        obj=abc.Get()
        inp=abc.input_to(obj)
        if inp == 'p':
            global_var.play*=-1
        if inp=='q':
                break
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
            ball.updatevar()
            ball.ball_wall()
            ball.ball_paddle()
            ball.lost()
            ball.render()
            print(global_var.over)
            if(global_var.over==0):
                break
            global_var.display.render()
    print("GAME OVER!")