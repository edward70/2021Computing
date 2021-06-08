import pygame
import sys
from random import randint

pygame.init()
screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("hi")
#img = pygame.image.load('photo.jpg')

clock = pygame.time.Clock()

WHITE = [255,255,255]
BLACK = [0,0,0]


gameOn = True
particles = []
while gameOn:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False

 #   screen.blit(img,(-300,0))

    particles.append([[250,260], [randint(-70,70)/100, randint(-200,-30)/100], randint(5,10)])
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[1][1] += 0.01
        particle[2] -= 0.01
        pygame.draw.circle(screen, WHITE, particle[0], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)

    clock.tick(100)
    pygame.display.flip()

sys.exit()