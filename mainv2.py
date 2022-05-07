from turtle import position
import pygame, sys, math, random
from pygame.locals import *
from pygame import mixer

#Init
size = (500,500)
pygame.init()
pygame.display.set_caption("Proyecto Álgebra Lineal")
screen = pygame.display.set_mode(size, 0, 32)
font = pygame.font.SysFont(None, 20)
clock=pygame.time.Clock()

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

#Atribute of click

click = False

#Main menu
def mainmenu(click):
    #pygame main
    while True:

        #What it shows in the screen
        screen.fill(WHITE)
        escribir("-- Proyecto Álgebra Lineal --",font,BLACK,screen,20,20)

        mx,my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(100,100,200,50)
        button_2 = pygame.Rect(100,200,200,50)

        if button_1.collidepoint((mx,my)):
            if click:
                up_map(click)
        
        if button_2.collidepoint((mx,my)):
            if click:
                credits()
        
        pygame.draw.rect(screen,RED,button_1)
        pygame.draw.rect(screen,RED,button_2)
        click = False

        #We define what does every key do
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


def up_map(click):

    running = True

    #Setting a new window name
    pygame.display.set_caption("Mapa")
    
    #Creating a surface object with our map and scaling it
    mapbackground = pygame.image.load("map.jpg")
    mapbackground = pygame.transform.scale(mapbackground,size)

    #Creating an user surface object and a user Marcador object
    user = pygame.image.load("playericon.png")
    user = pygame.transform.scale(user,(15,20))
    usercopy = user

    x = 0
    y = 0
    xspeed = 0
    yspeed = 0

    while running:
        escribir("- Mapa -",font,BLACK,screen,20,20)
    
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    running = False
            
                if event.key == K_w:
                    yspeed = -0.25
                    usercopy = pygame.transform.rotate(user,0)

                if event.key == K_s:
                    yspeed = 0.25
                    usercopy = pygame.transform.rotate(user,180)

                if event.key == K_d:
                    xspeed = 0.25
                    usercopy = pygame.transform.rotate(user,-90)

                if event.key == K_a:
                    xspeed = -0.25
                    usercopy = pygame.transform.rotate(user,90)
                
                if event.key == K_SPACE:
                    usercopy.get_rect()

            if event.type == pygame.KEYUP:
                if event.key == K_w:
                    yspeed = 0
                if event.key == K_s:
                    yspeed = 0
                if event.key == K_d:
                    xspeed = 0
                if event.key == K_a:
                    xspeed = 0
                   
        x += xspeed
        y += yspeed
        positionk = (x,y)
        userpos = font.render(str("Cordenadas objeto"+str(positionk)),True,(0,0,0))
        screen.blit(mapbackground,[0,0])
        screen.blit(usercopy,(x,y))
        screen.blit(userpos,(0,0))

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


mainmenu(click)
