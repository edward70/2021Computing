# Write your code here :-)
import pygame, time

pygame.init()
screen = pygame.display.set_mode([500,500])
RED = [255,0,0]
pygame.draw.rect(screen, RED, [0,0,250,250])
pygame.display.flip()
time.sleep(10)
pygame.quit()
