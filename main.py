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

#Init
pygame.init()
win=pygame.display.set_mode((1200,800))
pygame.display.set_caption("Proyecto Álgebra")
pygame.display.set_icon(linkchiquito)

#Cursor
pygame.mouse.set_cursor(*pygame.cursors.diamond)

#White
white=(255,255,255)

#Atributos y while:
x=10
y=10
while True:
    
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

    win.fill(white)
    win.blit(linkchiquito,(x,y))
    pygame.display.update()



    






   
            