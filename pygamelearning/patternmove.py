# Write your code here :-)
import pygame, time
import sys
from math import sin, pi

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([500,500])

WHITE = [255,255,255]
BLACK = [0,0,0]

screen.fill(WHITE)

x = 0
y = 0
while True:
    x = x+1
    y = y+0.1
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(100)
    pygame.draw.circle(screen,[0,0,0],[x,250+sin(0.5*y)*100],30)
    pygame.display.update()
    
    