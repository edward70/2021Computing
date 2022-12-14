import pygame
import sys
from random import randint
from math import sqrt

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([500, 550])
game_over = pygame.font.SysFont('monospace', 50).render('GAME OVER', True, (255, 0, 0))
win_screen = pygame.font.SysFont('monospace', 50).render('You Won! :)', True, (0, 255, 0))
play_again = pygame.font.SysFont('monospace', 20).render('press space to play again', True, (0, 0, 0))
font = pygame.font.SysFont('Arial', 20)
answer_font = pygame.font.SysFont('Arial', 16)

def question():
    signs = ["+" if randint(1,2) == 1 else "-" for i in range(3)]
    numbers = [randint(1,10) for i in range(3)]
    eq_body = "".join(["(x" + signs[i] + str(numbers[i]) + ")" for i in range(3)])
    soln = 1
    for i in range(len(numbers)):
        if signs[i] == "+":
            soln = soln * numbers[i]
        else:
            soln = soln * (-numbers[i])
    ans = answer_font.render(str(soln), True, (0,0,0))
    return ans, font.render(f'Find y-intercept of: y = {eq_body}', True, (255,255,255))

solution, question_text = question()

snake = [[randint(0,49), randint(0,49)]]

# init for genpos since otherwise it would be recursively dependent
fakeFood = []
foodPos = None
alive = True
win = False

def checkPlayable(head):
    global win
    for i in range(50):
        for j in range(50):
            coord = [i,j]
            dist = sqrt((coord[0]-head[0])**2 + (coord[1]-head[1])**2)
            if not coord in snake and dist > 3 and not coord in fakeFood and not coord == foodPos:
                return True

    print("You Won! Good job :)")
    win = True
    return False

def genPos():
    head = snake[len(snake)-1]
    count = 0
    while True:
        if count == 1000: # a bit inelegant
            if checkPlayable(head) == False:
                alive = False
                return [0,0]
        rand = [randint(0,49), randint(0,49)]
        dist = sqrt((rand[0]-head[0])**2 + (rand[1]-head[1])**2)
        if not rand in snake and dist > 3 and not rand in fakeFood and not rand == foodPos:
            return rand
        else:
            count = count + 1

def genFakeAnswer():
    while True:
        fake = randint(-1000,1000)
        if not fake == solution:
            return answer_font.render(str(fake), True, (0,0,0))

direction = "D"
foodPos = genPos()
score = 0
fakeAnswers = [genFakeAnswer() for i in range(score+1)]
fakeFood = [genPos() for i in range(score+1)]

while True:
    screen.fill([255,255,255])
    pygame.draw.rect(screen, [50,50,50], [0,0,500,50])

    score_text = font.render(f'Score: {score}', True, (255,255,255))
    screen.blit(score_text, (10,10))

    screen.blit(question_text, (120,10))

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
                    foodPos = genPos()
                    score = 0
                    alive = True
                    win = False
                    fakeAnswers = [genFakeAnswer() for i in range(score+1)]
                    fakeFood = [genPos() for i in range(score+1)]

    if alive == False:
        if win:
            screen.blit(win_screen,(100,250))
        else:
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

    if newEnd in snake or snake[end] in fakeFood:
        alive = False
    else:
        snake.append(newEnd)

    if snake[end] == foodPos:
        foodPos = genPos()
        fakeAnswers = [genFakeAnswer() for i in range(score+1)]
        fakeFood = [genPos() for i in range(score+1)]
        solution, question_text = question()
        score = score + 1
    else:
        snake.pop(0)

    pygame.draw.rect(screen, [255,255,0], [foodPos[0]*10,foodPos[1]*10+50,10,10])
    screen.blit(solution, (foodPos[0]*10 if foodPos[0] == 0 else foodPos[0]*10-10,foodPos[1]*10+50 if foodPos[1] == 0 else foodPos[1]*10+40))

    # disgusting code
    for j in range(len(fakeFood)):
        i = fakeFood[j]
        pygame.draw.rect(screen, [255,255,0], [i[0]*10,i[1]*10+50,10,10])
        screen.blit(fakeAnswers[j], (i[0]*10 if i[0] == 0 else i[0]*10-10,i[1]*10+50 if i[1] == 0 else i[1]*10+40))

    for i in snake:
        pygame.draw.rect(screen, [0,0,0], [i[0]*10,i[1]*10+50,10,10])

    clock.tick(10+score)
    pygame.display.flip()

pygame.quit()
