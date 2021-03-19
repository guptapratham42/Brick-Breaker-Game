#from global_var import *
import global_var
import colorama
from colorama import Fore, Back, Style
colorama.init()

class ufo:
    def __init__(self):
        self.padd_mat=([[ Fore.BLUE + "F" for i in range(global_var.paddle_length)] for j in range(2)])
    def render(self):
        self.padd_mat=([[ Fore.BLUE + "F" for i in range(global_var.paddle_length)] for j in range(2)])
        for i in range(2):
            for j in range(global_var.paddle_length):
                global_var.display.grid[i+1][global_var.paddle_mid-int(global_var.paddle_length/2)+j]=self.padd_mat[i][j]
    def clear(self):
        for i in range(2):
            for j in range(global_var.width):
                global_var.display.grid[i+1][j]=' '
    # def updatemid(self, val):
    #     if (self.temp - int(global_var.paddle_length/2)+ global_var.paddle_length < global_var.width-1) and val==2:
    #         self.temp+=val
    #     if (self.temp-int(global_var.paddle_length/2) >1) and val==-2:
    #         self.temp+=val
    #     global_var.paddle_start=self.temp-int(global_var.paddle_length/2)
    #     global_var.paddle_end=global_var.paddle_start+global_var.paddle_length
    #     global_var.paddle_mid=self.temp