import numpy as np
import pygame, sys
from pygame.locals import*

a=np.array([[2,4,6],[4,5,6],[3,1,-2]])
b=np.array([18,24,4])
x=np.linalg.solve(a,b)
print(x)

pygame.init()
win=pygame.display.set_mode((500,500))
img=pygame.imagen.load("unkown.png")
white=(255,255,255)
x=10
y=10
while True:
    for event in pygame.evente.ger():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_w:
                y=y-20
            if event.key==K_s:
                y=y+20
            if event.key==K_d:
                x=x+20
            if event.key==K_a:
                x=x-20
    win.fill(white)
    win.blit(img,(x,y))
    pygame.display.update()



            






   
            