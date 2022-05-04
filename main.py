from lib2to3.pygram import python_grammar_no_print_statement
import numpy as np
import pygame, sys
from pygame.locals import*


a=np.array([[2,4,6],[4,5,6],[3,1,-2]])
b=np.array([18,24,4])
x=np.linalg.solve(a,b)
print(x)


pygame.init()
pygame.mouse.set_cursor(*pygame.cursors.diamond)
bg=pygame.image.load("unknown.png")
win=pygame.display.set_mode((800,800))
pygame.display.set_caption("Proyecto Álgebra")
img=pygame.image.load("unknown.png")
white=(255,255,255)
x=10
y=10
while True:
    #gameDisplay.blit(bg,(800,800))
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
    win.blit(img,(x,y))
    pygame.display.update()



    






   
            