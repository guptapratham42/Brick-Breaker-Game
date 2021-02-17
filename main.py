import input as abc
import colorama
from colorama import Fore, Back, Style
import grid as grid
import global_var
import paddle
import time
import ball
import brick

colorama.init()
if __name__ == "__main__":
    padd=paddle.paddle()
    ball=ball.Ball()
    wb=brick.Brick()
    while (1):
        obj=abc.Get()
        inp=abc.input_to(obj)
        padd.clear()
        ball.clear()
        wb.clear()
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
        wb.render()
        if(global_var.over):
            break
        global_var.display.render()
    print("GAME OVER!")