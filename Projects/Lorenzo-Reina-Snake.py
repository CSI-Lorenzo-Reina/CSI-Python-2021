#recreate the screen
from ast import FloorDiv
from os import system
import pygame as pg
pg.init()           

purple = [134, 54, 255]    #food
darkpurple = [51,20,97]    #background 
lightpurple = [162,117,230]    #snake 
white = [0,0,0]              #gameover & score

dis=pg.display.set_mode((600,500))      #define screen resolution
#pg.display.update()                     #actualizes what happens on screen

pg.display.set_caption("Snake Game! by LR")

game_over=False       
x1 = 250
y1 = 250
x1_change= 0
y1_change= 0
clock = pg.time.Clock()

while not game_over:                    
    for event in pg.event.get():
        if pg.event==pg.QUIT:
            game_over=True                 #set it so the game doesnt close immediately
        if event.type == pg.KEYDOWN:       #set controls
            if event.key == pg.K_LEFT:
                x1_change = -10
                y1_change = 0
            if event.key == pg.K_RIGHT:
                x1_change = 10
                y1_change = 0
            if event.key == pg.K_UP:
                x1_change = 0
                y1_change = -10
            if event.key == pg.K_DOWN:
                x1_change = 0
                y1_change = 10
    x1 += x1_change                                      #update x position
    y1 += y1_change                                      #update y position

    dis.fill(darkpurple)                                 #set background color
    pg.draw.rect(dis, lightpurple,[x1,y1, 10, 10])       #spawn the snake
    
    pg.display.update() 

    clock.tick(20)
pg.quit()
quit()



