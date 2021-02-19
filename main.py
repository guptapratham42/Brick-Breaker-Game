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
        for j in range(1, 95, 10):
            bricksarray.append(brick.white_brick(i, j))
    for i in range(3, 8 ,4):
        for j in range(6, 95, 10):
            bricksarray.append(brick.yellow_brick(i, j))
    for i in range(1, 6 ,4):
        for j in range(6, 95, 10):
            bricksarray.append(brick.green_brick(i, j))
    for i in range(3, 8 ,4):
        for j in range(1, 95, 10):
            bricksarray.append(brick.unbreak_brick(i, j))
colorama.init()
if __name__ == "__main__":
    padd=paddle.paddle()
    ball=ball.Ball()
    # wb=brick.white_brick(3, 2)
    # yb=brick.yellow_brick(10,10)
    initial_bricks()
    while (1):
        obj=abc.Get()
        inp=abc.input_to(obj)
        padd.clear()
        ball.clear()
        #wb.clear()
        if inp != None:
            time.sleep(0.05)
        if inp=='q':
            break
        if inp=='d':
            padd.updatemid(2)
        if inp=='a':
            padd.updatemid(-2)
        ball.ball_wall()
        ball.ball_paddle()
        padd.render()
        ball.render()
        ball.lost()
        for i in bricksarray:
            i.render()
        # wb.render()
        # yb.render()
        #wb.abc()
        if(global_var.over):
            break
        global_var.display.render()
    print("GAME OVER!")