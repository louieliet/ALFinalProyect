import pygame, sys, math
from pygame.locals import *

#Init
size = (500,500)
pygame.init()
pygame.display.set_caption("Proyecto Álgebra Lineal")
screen = pygame.display.set_mode(size, 0, 32)
font = pygame.font.SysFont(None, 20)

#Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


def escribir(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)


click = False

def mainmenu():
    while True:
        screen.fill(WHITE)
        escribir("-- Proyecto Álgebra Lineal --",font,BLACK,screen,20,20)

        mx,my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(100,100,200,50)
        button_2 = pygame.Rect(100,200,200,50)

        if button_1.collidepoint((mx,my)):
            if click:
                up_map()
        
        if button_2.collidepoint((mx,my)):
            if click:
                credits()
        
        pygame.draw.rect(screen,RED,button_1)
        pygame.draw.rect(screen,RED,button_2)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def up_map():
    
    running = True

    while running:

        screen.fill(WHITE)

        escribir("- Mapa -",font,BLACK,screen,20,20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()


def credits():
    running = True

    while running:
        screen.fill(WHITE)

        escribir("- Integrantes: -",font,BLACK,screen,20,20)
        escribir("- Emi -",font,BLACK,screen,20,30)
        escribir("- Ari -",font,BLACK,screen,20,40)
        escribir("- Liz -",font,BLACK,screen,20,50)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()


mainmenu()
