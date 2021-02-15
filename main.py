import input as abc
import colorama
from colorama import Fore, Back, Style
import grid as grid
import global_var
import paddle

colorama.init()
if __name__ == "__main__":
    while (1):
        obj=abc.Get()
        inp=abc.input_to(obj)
        padd=paddle.paddle()
        #global_var.display(global_var.height, global_var.width)
        padd.clear()
        if inp=='q':
            break
        if inp=='d':
            # print("aaa")
            padd.updatemid(1)
        if inp=='a':
            padd.updatemid(-1)
        
        #print(global_var.paddle_mid)
        #paddle.render()
        padd.render()
        global_var.display.render()
        #print(inp)