from numpy import numpy
import pygame, sys
from pygame.locals import*

pygame.init()
win=pygame.display.set_mode((500,500))
img=pygame.imagen.load("descargar.png")
white=(255,255,255)
x=10
y=10
while True:
    for event in pygame.evente.ger():
        