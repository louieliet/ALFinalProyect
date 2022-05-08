import pygame, sys, math, random, os
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


#Define class user

class User(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((64, 54, 16, 16))

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
           self.rect.move_ip(-0.25, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move_ip(0.25, 0)
        if key[pygame.K_UP]:
           self.rect.move_ip(0, -0.25)
        if key[pygame.K_DOWN]:
           self.rect.move_ip(0, 0.25)

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), self.rect)


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


user = User()

def up_map(click):

    running = True

    #Setting a new window name
    pygame.display.set_caption("Mapa")
    
    #Creating a surface object with our map and scaling it
    mapbackground = pygame.image.load("map.jpg")
    mapbackground = pygame.transform.scale(mapbackground,size)

    while running:
        escribir("- Mapa -",font,BLACK,screen,20,20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(mapbackground,[0,0])

        user.draw(screen)
        user.handle_keys()
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
