import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 500])

image = pygame.image.load("baddie.png")
image_rect = image.get_rect(center=[250,250])

def rotated(picture, angle):
    picture_rotated = pygame.transform.rotozoom(picture,angle,1)
    picture_rotated_rect = picture_rotated.get_rect(center=[250,250])
    return picture_rotated, picture_rotated_rect

gameOn = True
angle = 0
x = 0
while gameOn == True:
    screen.fill([0,0,0])
    angle = angle - 1
    x = x + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    image_rotated, image_rotated_rect = rotated(image, angle)
    screen.blit(image_rotated, image_rotated.get_rect(center=[x,250]))
    clock.tick(100)
    pygame.display.flip()
pygame.quit()
