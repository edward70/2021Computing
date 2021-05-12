import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 500])
screen.fill([0,0,0])

image = pygame.image.load("baddie.png")
image_rect = image.get_rect(center=[250,250])

gameOn = True
while gameOn == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.blit(image, image_rect)
    clock.tick(100)
    pygame.display.flip()
pygame.quit()
