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

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
TEXTCOLOR = (  0,   0,  0)

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



def main():

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
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            draw_circle()
            pygame.display.update()
            

    x+=xspeed
    y+=yspeed
    positionk=(x,y)

    #RenderText
    kcoo=texto.render(str("Cordenadas objeto"+str(positionk)),True,(0,0,0))
    #pdist=texto.render(str("Distancia objeto-> punto"+str(dist)),True,(0,0,0))

    #Game
    win.blit(mapbg,[0,0])
    win.blit(playercopy,(x,y))
    win.blit(kcoo,(0,0))
    #win.blit(mcoo,(0,485))
    #win.blit(pdist,(300,0))
    pygame.display.update()
    clock.tick(60)



def get_pos():
    pos = pygame.mouse.get_pos()
    return (pos)

def draw_circle():
    pos=get_pos()
    pygame.draw.circle(mapbg, BLUE, pos, 20)

if __name__ == "__main__":
    main()

    






   
            