#recreate the screen
from ast import FloorDiv
from os import system
import pygame as pg
import time
pg.init()           

purple = [134, 54, 255]    #food
darkpurple = [51,20,97]    #background 
lightpurple = [162,117,230]    #snake 
white = [255,255,255]              #gameover & score

dis_width = 600
dis_height = 500

game_over=False   

clock = pg.time.Clock()
snake_speed= 15
snake_block= 10

pg.display.set_caption("Snake Game! by LR")

dis=pg.display.set_mode((dis_width,dis_height))      #define screen resolution
#pg.display.update()                     #actualizes what happens on screen

font_style = pg.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/2.5])

def gameloop():
    game_over = False
    game_close = False
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change= 0
    y1_change= 0

    while not game_over:     
        while game_close == True:
            dis.fill(darkpurple)
            message("GAME OVER! Press C- Play again or N- Quit", white)
            pg.display.update()

            for event in pg.event.get():
                if event.type==pg.KEYDOWN:
                    if event.key == pg.K_n:
                        game_over = True
                        game_close = False
                    if event.key == pg.K_c:
                        gameloop()
                       
        for event in pg.event.get():
            if pg.event==pg.QUIT:
                game_over=True                 #set it so the game doesnt close immediately
            if event.type == pg.KEYDOWN:       #set controls
                if event.key == pg.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pg.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pg.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pg.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

    x1 += x1_change                                      #update x position
    y1 += y1_change                                      #update y position

    dis.fill(darkpurple)                                 #set background color
    pg.draw.rect(dis, lightpurple,[x1,y1, snake_block, snake_block])       #spawn the snake
    
    pg.display.update() 

    clock.tick(snake_speed)

message("GAME OVER!", white)
#pg.display.update()
#time.sleep(5)
pg.quit()
quit()



