import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 500])

gameOn = True
x = 0
y = 100
direction = 'x'
while gameOn == True:
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            if direction == 'x':
                direction = 'y'
            else:
                direction = 'x'
    
    if direction == 'x':
        x = x + 1
    else:
        y = y + 1

    pygame.draw.circle(screen, [0,0,0], [x,y], 10)
            
    clock.tick(100)
    pygame.display.flip()
pygame.quit()
