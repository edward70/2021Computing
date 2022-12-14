import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 500])

gameOn = True
x1 = 0
y1 = 100
x2 = 100
y2 = 0
while gameOn == True:
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if x1 == 500:
        moveRight = False
    elif x1 == 0:
        moveRight = True
    
    if y2 == 500:
        moveDown = False
    elif y2 == 0:
        moveDown = True
        
    if moveRight:
        x1 = x1+1
    else:
        x1 = x1-1

    if moveDown:
        y2 = y2+1
    else:
        y2 = y2-1

    pygame.draw.circle(screen, [0,0,0], [x1,y1], 10)
    pygame.draw.rect(screen, [0,0,0], [x2,y2,30,30])
            
    clock.tick(100)
    pygame.display.flip()
pygame.quit()
