from cgitb import text
from lib2to3.pygram import python_grammar_no_print_statement
import pygame, sys
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




while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
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

        if event.type==pygame.KEYUP:
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


    positionm=pygame.mouse.get_pos()
    positionk=(x,y)
    dist = math.sqrt((positionm[0]-positionk[0])**2 + (positionm[1]-positionk[1])**2)

    #RenderText
    kcoo=texto.render(str("Cordenadas objeto"+str(positionk)),True,(0,0,0))
    mcoo=texto.render(str("Cordenadas mouse"+str(positionm)),True,(0,0,0))
    pdist=texto.render(str("Distancia objeto -> mouse"+str(dist)),True,(0,0,0))

    #Game
    win.blit(mapbg,[0,0])
    win.blit(playercopy,(x,y))
    win.blit(kcoo,(0,0))
    win.blit(mcoo,(0,485))
    win.blit(pdist,(300,0))
    pygame.display.update()
    clock.tick(60)


    
    

    






   
            