from cgitb import text
from lib2to3.pygram import python_grammar_no_print_statement
import pygame, sys, time
from pygame.locals import*
import math
import random
from pygame import mixer


#Init Pygame
pygame.init()
size=(734,508)
pygame.display.set_caption("Proyecto Álgebra")
win=pygame.display.set_mode(size)


clock=pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TEXTCOLOR = (0, 0, 0)

#Init bgmap
maporiginal=pygame.image.load("map.jpg")
mapbg=pygame.transform.scale(maporiginal,size)

#Init icon
mapicon=pygame.image.load("mapicon.png")
pygame.display.set_icon(mapicon)

#Init Player
playermaximized=pygame.image.load("playericon.png")
player=pygame.transform.scale(playermaximized,(15,20))

#Text
texto=pygame.font.SysFont(None,30)
texto2=pygame.font.SysFont(None,20)

#Atributos y while:
playercopy=player

#Text
texto=pygame.font.SysFont(None,30)

x = 0
y = 0

xspeed = 0
yspeed = 0
red=(255,0,0)


class Marcador():
    def drawposition(self):
        pos=pygame.mouse.get_pos()
        pygame.draw.circle(mapbg,BLUE,pos,5)

m1=Marcador()

#Main:

while True:

#Mientras corra el juego:
    for event in pygame.event.get():
        #Cierre del juego
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

#Si presionamos una telca:
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                yspeed = -2
                playercopy=pygame.transform.rotate(player,0)
            if event.key==K_s:
                yspeed = 2
                playercopy=pygame.transform.rotate(player,180)
            if event.key==K_d:
                xspeed = 2
                playercopy=pygame.transform.rotate(player,-90)
            if event.key==K_a:
                xspeed = -2
                playercopy=pygame.transform.rotate(player,90)

            if event.key==K_SPACE:
                m1.drawposition()

#Si dejamos de presionar las telcas:
        if event.type == pygame.KEYUP:
            if event.key==K_w:
                yspeed=0
            if event.key==K_s:
                yspeed=0
            if event.key==K_d:
                xspeed=0
            if event.key==K_a:
                xspeed=0
        
        

    x+=xspeed
    y+=yspeed
    positionk=(x,y)

    #RenderText
    COORDENADAS_OBJETO=texto.render(str("Cordenadas objeto"+str(positionk)),True,(0,0,0))

    #Game

    #Background map
    win.blit(mapbg,[0,0])
    #Display object
    win.blit(playercopy,(x,y))
    #Display position of object text
    win.blit(COORDENADAS_OBJETO,(0,0))



    #Do not touch
    pygame.display.update()
    clock.tick(60)








    






   
            