#recreate the screen
from ast import FloorDiv
import pygame as pg
pg.init()           

purple = [134, 54, 255]    #food
darkpurple = [51,20,97]    #background 
lightpurple = [162,117,230]    #snake 
white = [0,0,0]    #gameover & score

dis=pg.display.set_mode((600,500))      #define screen resolution
#pg.display.update()                     #actualizes what happens on screen

pg.display.set_caption("Snake Game! by LR")
game_over=False                        
while not game_over:                     #set it so the game doesnt close immediately
    for event in pg.event.get():
        if pg.event==pg.QUIT:
            game_over=True
    pg.draw.rect(dis, lightpurple,[300,250, 10, 10])      #spawn the snake
    pg.display.update() 

pg.quit()
quit()



