import pygame, sys, math, random 
from pygame.locals import *
from pygame import mixer


#Init
size = (500,500)
pygame.init()
pygame.display.set_caption("Proyecto Álgebra Lineal")
screen = pygame.display.set_mode(size, 0, 32)
font = pygame.font.SysFont(None, 20)
menutitle = pygame.font.SysFont(None, 45)
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

        menubg = pygame.image.load("mathbg.jpg") 
        menubg = pygame.transform.scale(menubg,size)  
        screen.blit(menubg,(0,0))
        escribir("-- Proyecto Álgebra Lineal --",menutitle,WHITE,screen,45,50)

        mx,my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(145,160,200,50)
        button_2 = pygame.Rect(145,240,200,50)

        if button_1.collidepoint((mx,my)):
            if click:
                up_map()
        
        if button_2.collidepoint((mx,my)):
            if click:
                credits()
        
        pygame.draw.rect(screen,RED,button_1)
        menu_font=pygame.font.SysFont("Hevetica",30)
        escribir("Consultar Mapa",menu_font,WHITE,screen,165,175)
        pygame.draw.rect(screen,RED,button_2)
        escribir("Creditos",menu_font,WHITE,screen,200,255)
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

def up_map():

    running = True
    
    x = 0
    y = 0
    xspeed = 0
    yspeed = 0

    x2 = 0
    y2 = 0
    x2speed = 0
    y2speed = 0

    #Setting a new window name
    pygame.display.set_caption("Mapa")
    
    #Creating a surface object with our map and scaling it to put it as background
    mapbackground = pygame.image.load("map.jpg")
    mapbackground = pygame.transform.scale(mapbackground,size)

    marcador = pygame.image.load("marcador.jpg")
    marcador = pygame.transform.scale(marcador,(10,10))

    #Creating an surface object called user and its rect
    user = pygame.image.load("playericon.png")
    user = pygame.transform.scale(user,(15,20))
    usercopy = user
    user_rect = user.get_rect()

    user2 = pygame.image.load("playericon2.png")
    user2 = pygame.transform.scale(user2,(15,20))
    user2copy = user2
    

    while running:
        escribir("- Mapa -",font,BLACK,screen,20,20)
        
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key==K_w:
                    yspeed = -1
                    usercopy=pygame.transform.rotate(user,0)
                if event.key==K_s:
                    yspeed = 1
                    usercopy=pygame.transform.rotate(user,180)
                if event.key==K_d:
                    xspeed = 1
                    usercopy=pygame.transform.rotate(user,-90)
                if event.key==K_a:
                    xspeed = -1
                    usercopy=pygame.transform.rotate(user,90)

                if event.key==K_UP:
                    y2speed = -1
                    user2copy=pygame.transform.rotate(user2,0)
                if event.key==K_DOWN:
                    y2speed = 1
                    user2copy=pygame.transform.rotate(user2,180)
                if event.key==K_RIGHT:
                    x2speed = 1
                    user2copy=pygame.transform.rotate(user2,-90)
                if event.key==K_LEFT:
                    x2speed = -1
                    user2copy=pygame.transform.rotate(user2,90)

                if event.key == K_ESCAPE:
                    running = False

            
            if event.type == pygame.KEYUP:
                if event.key==K_w:
                    yspeed=0
                if event.key==K_s:
                    yspeed=0
                if event.key==K_d:
                    xspeed=0
                if event.key==K_a:
                    xspeed=0
                    
                if event.key==K_UP:
                    y2speed=0
                if event.key==K_DOWN:
                    y2speed=0
                if event.key==K_RIGHT:
                    x2speed=0
                if event.key==K_LEFT:
                    x2speed=0


        x += xspeed
        y += yspeed
        user_position = (x,y)

        x2 += x2speed
        y2 += y2speed
        user2_position = (x2,y2)
   
        dist = int(math.sqrt((x-x2)**2 + (y-y2)**2))

        kcoo_font = pygame.font.SysFont("Helvetica",15)
        mcoo_font = pygame.font.SysFont("Helvetica",15)
        pdist_font = pygame.font.SysFont("Helvetica",15)


        mcoo = mcoo_font.render(str("Cordenadas persona 2: "+str(user2_position)),True,(255,255,255),(0,0,0))
        kcoo = kcoo_font.render(str("Cordenadas persona 1: "+str(user_position)),True,(255,255,255),(0,0,0))
        pdist = pdist_font.render(str("Distancia entre los dos puntos: "+str(dist)),True,(255,255,255),(0,0,0))
                
        screen.blit(mapbackground,(0,0))
        screen.blit(pdist,(0,0))
        screen.blit(usercopy,(x,y))
        screen.blit(user2copy,(x2,y2))
        screen.blit(kcoo,(0,460))
        screen.blit(mcoo,(0,480))
 

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
