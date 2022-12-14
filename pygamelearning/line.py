# Write your code here :-)
import pygame, time
import sys

pygame.init()
screen = pygame.display.set_mode([500,500])

WHITE = [255,255,255]
BLACK = [0,0,0]

screen.fill(WHITE)
pygame.draw.lines(screen, BLACK, False, [[50,50],[250,100]], 5)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
