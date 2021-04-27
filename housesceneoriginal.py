# Write your code here :-)
import pygame, time
from random import randint
from math import sin,cos,pi
import sys

FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([500,500])

YELLOW = [255,255,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
BROWN = [210,105,30]
RED = [255,0,0]
WHITE = [255,255,255]
BLACK = [0,0,0]
GREY = [50,50,50]
CYAN = [0,255,255]
DARK_GREEN = [0,100,0]

grass = []
for i in range(60):
    grass.append([randint(0,480), randint(270,480)])

clouds = []
for i in range(1,6): # cloud generation (proud of this one :)
        a = randint((400/5)*(i-1),(400/5)*i)
        b = randint(0,130)
        c = randint(70,120)
        d = randint(20,30)
        for j in range(10):
            clouds.append([a+randint(-20,20),b+randint(-20,20),c+randint(-20,20),d])

ticks = 0
while True:
    pygame.draw.rect(screen, BLUE, [0,0,500,500]) # sky
    pygame.draw.rect(screen, GREEN, [0,250,500,250]) # grass

    for i in range(60): # grass spots
        pygame.draw.circle(screen, DARK_GREEN, grass[i], 5)

    pygame.draw.circle(screen, YELLOW, [0,0], 100) # sun
    for i in range(10): # 0->9 loop
        j = pi * i * 10 / 180 # degrees to radians
        l = sin(j)*130 # trig is awesome
        w = cos(j)*130
        pygame.draw.lines(screen, YELLOW, False, [[0, 0],[l,w]], 5)

    pygame.draw.rect(screen, BROWN, [250,270,100,100]) # house
    pygame.draw.rect(screen, BROWN, [330,220,20,50]) # chimney
    pygame.draw.ellipse(screen, GREY, [330,205,30,20]) # smoke
    pygame.draw.ellipse(screen, GREY, [330,190,50,20]) # smoke
    pygame.draw.ellipse(screen, GREY, [330,180,70,20]) # smoke
    pygame.draw.polygon(screen, RED, [[300,170],[250,270],[350,270]]) # roof
    pygame.draw.rect(screen, WHITE, [290,320,20,50]) # door
    pygame.draw.circle(screen, BLACK, [295,345],5) # door knob
    pygame.draw.rect(screen, BLACK, [0,400,500,70]) # road
    pygame.draw.rect(screen, BROWN, [100,270,20,100]) # tree
    pygame.draw.circle(screen, DARK_GREEN, [110,270], 50) # leaves

    for i in range(50):
        pygame.draw.ellipse(screen, WHITE, [(clouds[i][0]+ticks)%600, clouds[i][1], clouds[i][2], clouds[i][3]])

    for i in range(17):
        pygame.draw.rect(screen, WHITE, [i*30,425,20,10]) # road lines

    pygame.draw.rect(screen, BLUE, [100+ticks*2,400,100,50]) # car
    pygame.draw.ellipse(screen, GREY, [180+ticks*2,450,20,20]) # wheel
    pygame.draw.ellipse(screen, GREY, [100+ticks*2,450,20,20]) # wheel
    pygame.draw.rect(screen, CYAN, [170+ticks*2,400,30,25]) # window
    pygame.draw.rect(screen, BLACK, [100+ticks*2,400,20,25]) # remove edge
    pygame.draw.rect(screen, BLACK, [190+ticks*2,400,10,25]) # remove edge
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
    ticks = ticks + 1
