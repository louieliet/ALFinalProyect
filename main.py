from lib2to3.pygram import python_grammar_no_print_statement
import numpy as np
import pygame, sys
from pygame.locals import*
import math
import random
from pygame import mixer


a=np.array([[2,4,6],[4,5,6],[3,1,-2]])
b=np.array([18,24,4])
x=np.linalg.solve(a,b)
print(x)


#Player
quintero=pygame.image.load("quintero.jpg")
link=pygame.image.load("icon.png")
linkchiquito=pygame.transform.scale(link,(50,50))
quinterobg=pygame.transform.scale(quintero,(500,500))

#Init
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Proyecto Álgebra")
pygame.display.set_icon(linkchiquito)

#Cursor
pygame.mouse.set_cursor(*pygame.cursors.diamond)

#White
white=(255,255,255)

#Text
texto=pygame.font.SysFont(None,30)
texto2=pygame.font.SysFont(None,20)

#RenderText
label=texto.render("Quintero Chiquito",True,(255,255,255))
label2=texto2.render("Yo era bonito y bien estudioso de morro, pero me lastime la rodilla",True,(0,0,0))

#Atributos y while:
x=10
y=10
linkrotating=0

while True:
    
    linkrotating+=1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_w:
                y=y-80
            if event.key==K_s:
                y=y+80
            if event.key==K_d:
                x=x+80
            if event.key==K_a:
                x=x-80
    linkchiquitocopy=pygame.transform.rotate(linkchiquito,linkrotating)

    win.blit(quinterobg,[0,0])
    win.blit(linkchiquitocopy,(x,y))
    win.blit(label,(160,40))
    win.blit(label2,(50,450))
    pygame.display.update()



    






   
            