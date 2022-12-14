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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            downPos = pygame.mouse.get_pos()
            circles.append(list(downPos))

    for i in range(len(circles)):
        a = circles[i]
        a[0] = a[0]+1
        pygame.draw.circle(screen, [0,0,0], a, 10)
            
    clock.tick(100)
    pygame.display.flip()
pygame.quit()
