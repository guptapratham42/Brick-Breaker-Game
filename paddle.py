from global_var import *
import colorama
from colorama import Fore, Back, Style
colorama.init()

class paddle:
    def __init__(self):
        self.temp=paddle_mid
        self.padd_mat=([[ Fore.BLUE + "O" for i in range(paddle_length)] for j in range(2)])
    def render(self):
        # print(self.temp)
        for i in range(2):
            for j in range(paddle_length):
                display.grid[height-2+i][self.temp-int(paddle_length/2)+j]=self.padd_mat[i][j]
    def clear(self):
        for i in range(2):
            for j in range(paddle_length):
                display.grid[height-2+i][self.temp-int(paddle_length/2)+j]=' '
    def updatemid(self, val):
        self.temp+=val
        paddle_mid=self.temp