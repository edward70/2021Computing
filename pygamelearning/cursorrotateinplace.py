import pygame
import sys
from math import pi, atan2

pygame.init()

screen = pygame.display.set_mode([500, 500])

gameOn = True
angle = 0
centre = (250,250)
image = pygame.transform.scale(pygame.image.load("turn.png"), (100,100))
image_rect = image.get_rect(center=centre)

def rotated(picture, angle):
    picture_rotated = pygame.transform.rotozoom(picture,angle,1)
    picture_rotated_rect = picture_rotated.get_rect(center=centre)
    return picture_rotated, picture_rotated_rect

def cartesian(x,y,centre):
    return x-centre[0],centre[1]-y

while gameOn == True:
    screen.fill([255,255,255])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mouse = pygame.mouse.get_pos()
    mouseCoords = cartesian(*mouse, centre)
    angle = -90 + atan2(*reversed(mouseCoords)) * (180/pi)

    image_rotated, image_rotated_rect = rotated(image, angle)
    screen.blit(image_rotated, image_rotated_rect)
    pygame.display.flip()
