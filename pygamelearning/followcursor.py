import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 500])

gameOn = True
circles = []
while gameOn == True:
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.circle(screen, [0,0,0], list(pygame.mouse.get_pos()), 10)
            
    clock.tick(100)
    pygame.display.flip()
pygame.quit()
