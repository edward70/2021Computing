import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 500])
screen.fill([255,255,255])

downPos = None
gameOn = True
while gameOn == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif not downPos and event.type == pygame.MOUSEBUTTONDOWN:
            downPos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            upPos = pygame.mouse.get_pos()
            pygame.draw.lines(screen, [0,0,0], False, [list(downPos),list(upPos)], 7)
            downPos = None
            
    clock.tick(100)
    pygame.display.flip()
pygame.quit()
