# Write your code here :-)

import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 500])

WHITE = [255, 255, 255]
y = 0

gameOn = True
while gameOn == True:
    y = y + 1
    screen.fill([0, 0, 0])
    pygame.draw.circle(screen, [0, 0, y % 255], [y, 250], 30)

    clock.tick(100)

    pygame.display.flip()
    if y > 500:
        gameOn = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
pygame.quit()
