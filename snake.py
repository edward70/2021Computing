import pygame
import sys
from random import randint

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 550])
game_over = pygame.font.SysFont('monospace', 50).render('GAME OVER', True, (255, 0, 0))
play_again = pygame.font.SysFont('monospace', 20).render('press space to play again', True, (0, 0, 0))
score_font = pygame.font.SysFont('Arial', 20)

snake = [[randint(0,49), randint(0,49)]]
direction = "D"
foodPos = [randint(0,49), randint(0,49)]
score = 0
alive = True

while True:
    screen.fill([255,255,255])
    pygame.draw.rect(screen, [50,50,50], [0,0,500,50])

    score_text = score_font.render(f'Score: {score}', True, (255,255,255))
    screen.blit(score_text, (10,10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if not direction == "S" or score == 0:
                    direction = "W"
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if not direction == "W" or score == 0:
                    direction = "S"
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if not direction == "A" or score == 0:
                    direction = "D"
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if not direction == "D" or score == 0:
                    direction = "A"
            if event.key == pygame.K_SPACE:
                if alive == False:
                    snake = [[randint(0,49), randint(0,49)]]
                    direction = "D"
                    foodPos = [randint(0,49), randint(0,49)]
                    score = 0
                    alive = True

    if alive == False:
        screen.blit(game_over,(100,250))
        screen.blit(play_again,(100,300))
        pygame.display.flip()
        continue

    end = len(snake) - 1
    if direction == "W":
        newEnd = [snake[end][0],(snake[end][1] - 1) % 50]
    elif direction == "A":
        newEnd = [(snake[end][0] - 1)%50,snake[end][1]]
    elif direction == "S":
        newEnd = [snake[end][0],(snake[end][1] + 1)%50]
    elif direction == "D":
        newEnd = [(snake[end][0] + 1)%50,snake[end][1]]

    if snake[end] == foodPos:
        foodPos = [randint(0,49), randint(0,49)]
        score = score + 1
    else:
        snake.pop(0)

    if newEnd in snake:
        alive = False
    else:
        snake.append(newEnd)

    pygame.draw.rect(screen, [255,0,0], [foodPos[0]*10,foodPos[1]*10+50,10,10])

    for i in snake:
        pygame.draw.rect(screen, [0,0,0], [i[0]*10,i[1]*10+50,10,10])

    clock.tick(10+score)
    pygame.display.flip()

pygame.quit()
