import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 500])
screen.fill([255,255,255])

gameOn = True
down = False
while gameOn == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            down = False
            
    if down == True:
        x,y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, [0,0,0], [x,y], 10)
    clock.tick(100)
    pygame.display.flip()
pygame.quit()
