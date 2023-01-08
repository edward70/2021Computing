from random import randint # import function to generate random integer

# unicode symbols for powers so python can display the polynomials properly
squared = "²"
cubed = "³"
quartic = "⁴"
quintic = "⁵"

# generate polynomial in the form y = (x+3)(x-6)³ etc.
def generate_factorised(degree, nfactors): # accept degree of polynomial and number of factors
    string = ["y = "] # use list to build question string because this allows gradual construction without string duplication
    xints = [] # store list of xintercepts
    #powers = []

    for factor in range(nfactors): # create correct number of factors
        number = randint(-18,18)/2 # generate random root
        sign = "+" if number >= 0 else "" # generate random sign

        power = randint(1,degree) # create a power
        #powers.append(power)
        if power == 1:
            power = "" # degree of one has no power
        elif power == 2:
            power = squared # degree of 2 squared
        elif power == 3:
            power = cubed # degree of 3 cubed
        elif power == 4:
            power = quartic # and so on
        elif power == 5:
            power = quintic # and so on
            
        string.append("(x{}{:g}){}".format(sign, number, power)) # format root into string
        xints.append(-number) # append x-intercept
    
    return "".join(string), xints # return question string and x-intercepts

import pygame # import pygame
import sys # import sys
# import the pytmx library for opening a level map file. i included this library with the code but i didn't write it
# https://github.com/bitcraft/pytmx
from pytmx.util_pygame import load_pygame

# colors with lists
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]

pygame.mixer.pre_init(44100, 16, 2, 4096) # init pygame's mixer
pygame.init() # init pygame
screen = pygame.display.set_mode([512, 512]) # set window dimensions
pygame.display.set_caption("Legend of the Polynomial Sketcher") # set window title
clock = pygame.time.Clock() # initialize pygame clock
font = pygame.font.SysFont('Arial', 14) # initialize game font
graphingFont = pygame.font.SysFont('Arial', 16, bold=True) # font for graphing
graph = pygame.transform.smoothscale(pygame.image.load("game_assets/graph.png").convert(), (512,512)) # load graph
graphdims = ((33/639*512, 610/639*512), (30/639*512+50, 607/639*512+50)) # find dimensions

# load main character
# i load the character as a map because i want to switch between the sprites
mainCharacterMap = load_pygame('game_assets/maincharacter.tmx') # load the character spritesheet as a map
mainCharacterSprites = [] # make a list for all the sprites
for layer in mainCharacterMap.layers: # loop though map layers
    for x, y, image in layer.tiles(): # loop through tiles in layer
        mainCharacterSprites.append(image) # add image of tile to sprite list
        
# load map
level1 = load_pygame('game_assets/level1.tmx') # load the first level
level2 = load_pygame('game_assets/level2.tmx') # load second
level3 = load_pygame('game_assets/level3.tmx') # load third
level4 = load_pygame('game_assets/level4.tmx') # load fourth
level5 = load_pygame('game_assets/level5.tmx') # load last
levels = [level1, level2, level3, level4, level5] # put levels in a list

# set properties for enemies
enemies = [["game_assets/enemy1.png", 15, 10], ["game_assets/enemy2.png", 15, 3], ["game_assets/enemy3.png", 15, 8], ["game_assets/enemy4.png", 15, 8], ["game_assets/enemy5.png", 14, 8]]
bonusenemy = ["game_assets/bonusenemy.png", 13, 8]

# game variables
gameOn = True
currentLevel = 0 # the current level of the rpg
characterX = 0 # the tile x position (not pygame x position) of the character
characterY = 4 # same for y position
moveDirection = None # the direction of a main character movement in progress
moveFrame = 0 # the current frame of the movement animation
spriteNumber = 0 # the number of the main character sprite
currentDialogue = ("You: I can use WASD to move", "This game's coder must be really smart B)") # the current dialogue line as a tuple
# i use a global mode switch to flip between graphing and RPG modes because this makes the code simpler
graphing = False # keep track of if currently in graphing

# function to redraw map, characters, dialogue
# i put this all in one function to make the code a bit cleaner
def updateRPG():
    # global variables are bad practice but this game is small so it doesn't really matter and nobody is watching
    global currentLevel # declare as global variables so they can modified inside the function
    global characterX
    global characterY
    global currentDialogue
    global graphing
    
    if characterX == 16: # check if character has gone off end the screen
        currentLevel += 1 # go to next level
        characterX = 0 # rollback player to start of screen
    elif characterX == -1: # check if character has gone off start of screen
        characterX = 0 # prevent them going off the screen
        currentDialogue = ("It's too late to go back now!", "Try going the other way.") # tell them to go the other way
    
    layerNumber = 0 # keep track of the current layer with a variable
    for layer in levels[currentLevel].layers: # loop layers of tilemap
        for x, y, image in layer.tiles(): # loop coordinates and images of tiles
            screen.blit(pygame.transform.scale(image, (32, 32)), (x * 32, y * 32)) # render upscaled tiles
            
            if layerNumber == 2 and x == characterX and y == characterY: # collision detection for solid objects
                if moveDirection == "w": # check if they are walking up
                    characterY += 1 # move them down to prevent them phasing through solid objects
                elif moveDirection == "s": # check if down
                    characterY -= 1 # move up
                elif moveDirection == "a": # check if left
                    characterX += 1 # move right
                elif moveDirection == "d": # check if right
                    characterX -= 1 # move left
            
        if layerNumber == 2: # render player before overlay decor (ie bushes) so the order is done properly
            screen.blit(pygame.transform.scale(pygame.image.load(enemies[currentLevel][0]), (32, 32)), (enemies[currentLevel][1] * 32, enemies[currentLevel][2] * 32)) # render enemy
            
            if currentLevel == 3:
                screen.blit(pygame.transform.scale(pygame.image.load(bonusenemy[0]), (32, 32)), (bonusenemy[1] * 32, bonusenemy[2] * 32)) # render enemy
            
            if characterY == enemies[currentLevel][2] and characterX == enemies[currentLevel][1]:
                characterX -= 1 # move left
                currentDialogue = ("A thug blocks the way. To get past you need", "to challenge them in a MATH duel (press e)")
            if currentLevel == 3 and characterY == bonusenemy[2] and characterX == bonusenemy[1]:
                characterX -= 1 # move left
                # its not a bug its a feature!!
                currentDialogue = ("You go stand in front of the thug", "to challenge them in a MATH duel press e")
                
            screen.blit(pygame.transform.scale(mainCharacterSprites[spriteNumber], (32, 32)), (characterX * 32, characterY * 32)) # render upscaled player with correct sprite number
        layerNumber += 1 # increment layer counter
        
    dialogue(currentDialogue[0], currentDialogue[1]) # display current dialogue lines
    currentDialogue = (None, None) # erase dialogue for next render
    screen.blit(graphingFont.render("Level: {}".format(currentLevel+1), True, WHITE), (5,5)) # render text
    screen.blit(graphingFont.render("Score: {}".format(globalscore), True, WHITE), (100,5)) # render text

# dialogue function
def dialogue(text, text2):
    if text or text2: # check if there is text to be displayed
        pygame.draw.rect(screen, BLACK, [112,450,300,50]) # draw the text box
    if text:
        screen.blit(font.render(text, True, WHITE), (120,460)) # draw the first line of text if it exists
    if text2:
        screen.blit(font.render(text2, True, WHITE), (120,475)) # draw the second line of text if it exists
   
# create question
qtext, bqints = generate_factorised(5, currentLevel+1) # generate question and backup intercepts
qints = bqints.copy() # copy backup to normal
xlist = [] # init xlist
poslist = [] # init poslist
question = graphingFont.render(qtext, True, RED) # render question text
score = 0 # init score
globalscore = 0

# mouse handling variables
mouseheld = False
lastpos = None
   
# i create a function to interpolate the line so that there aren't awkward gaps because of pygame's input lag     
# based on https://stackoverflow.com/questions/597369/how-to-create-ms-paint-clone-with-python-and-pygame
def roundline(srf, color, start, end, radius=3):
    global score # modify score
    dx = end[0]-start[0] # find difference in x
    dy = end[1]-start[1] # difference in y
    distance = max(abs(dx), abs(dy)) # find distance
    for i in range(distance): # loop distance
        x = int( start[0]+float(i)/distance*dx) # interpolate x
        y = int( start[1]+float(i)/distance*dy) # interpolate y
        xnum = x/(graphdims[0][1]-graphdims[0][0])*18-10 # convert to cartesian
        ynum = -(y/(graphdims[1][1]-graphdims[1][0])*18-10) # convert to cartesian
        
        #if x in xlist and not (x,y) in poslist:
        #    score = -1000
        #    print("not a function")
        xlist.append(x) # append to xlist
        poslist.append((x,y)) # add to position list
                    
        for q in qints: # loop through x-ints
            if abs(xnum - q) <= 0.2 and abs(ynum) <= 0.2: # check if close to xintercept
                score += 1 # increment score
                qints.remove(q) # remove from intercepts
                #print(score)
        pygame.draw.circle(srf, color, (x, y), radius) # draw circle

def clear_screen(): # clear screen for graph mode
    screen.blit(graph, [0,0]) # draw graph
    screen.blit(question, (5,5)) # draw question
    screen.blit(font.render("Press c to clear or v to submit", True, RED), (300,5)) # render text

# display starting image
screen.blit(pygame.transform.scale(pygame.image.load("game_assets/start.png"), (870,512)), (-179,0))
pygame.mixer.music.load('game_assets/ambient.ogg') # load background music
pygame.mixer.music.play(-1, 0.0) # play on repeat

# i keep track of the tutorial slide so the right one is displayed
tutorial = 1 # first tutorial slide

while gameOn: # run if game is on
    for event in pygame.event.get(): # handle events
        if event.type == pygame.QUIT: # handle quit event
            pygame.quit() # exit game
            sys.exit() # exit console
        if event.type == pygame.KEYDOWN and not graphing:
            if tutorial == 1: # display first tutorial slide
                screen.blit(pygame.image.load("game_assets/info.png"), (0,0))
                tutorial += 1
            elif tutorial == 2: # second slide
                screen.blit(pygame.image.load("game_assets/info2.png"), (0,0))
                tutorial = None
                continue
                                
            if tutorial == None: # display RPG once tutorial is over             
                updateRPG()
            if event.key == pygame.K_e: # handle enemy interact
                # check next to enemy
                if characterX == enemies[currentLevel][1] - 1 and characterY == enemies[currentLevel][2]:
                    graphing = True # enable graphing
                    clear_screen() # display graph
                if currentLevel == 3 and characterX == bonusenemy[1] - 1 and characterY == bonusenemy[2]:
                    graphing = True
                    clear_screen()
        
        if graphing: # check if in graph mode
            pos = pygame.mouse.get_pos() # get mouse position
            if event.type == pygame.MOUSEBUTTONDOWN: # check if mouse is down
                mouseheld = True # determine if mouse is held down
                lastpos = pos # set start position
            elif event.type == pygame.MOUSEBUTTONUP: # check if mouse is up
                mouseheld = False # the mouse is no longer held down
            elif event.type == pygame.MOUSEMOTION: # check if mouse moves
                xnum = pos[0]/(graphdims[0][1]-graphdims[0][0])*18-10 # convert xcoord to cartesian
                ynum = -(pos[1]/(graphdims[1][1]-graphdims[1][0])*18-10) # convert ycoord to cartesian
            
                if mouseheld: # check if mouse is held
                    #print(ynum)
                    for q in qints: # loop through intercepts
                        if abs(xnum - q) <= 0.2 and abs(ynum) <= 0.2: # check if line is close to intercept
                            score += 1 # increment score
                            qints.remove(q) # remove intercept
                            #print(score)
                    if pos[0] in xlist and not pos in poslist: # check if the graph is actually a function not a relation
                        highestdiff = 0 # keep track of highest distance in duplicates to prevent false positive
                        for item in poslist:
                            if pos[0] == item[0] and abs(pos[1] - item[1]) > highestdiff: # calculate highest diff
                                highestdiff = abs(pos[1] - item[1]) # set diff
                        if highestdiff > 20: # if diff is too large
                            score = -1000 # disqualified
                            print("not a function")
                    xlist.append(pos[0]) # add x to xlist
                    poslist.append(pos) # add pos to poslist
                    pygame.draw.circle(screen, BLACK, pos, 3) # draw circle
                    roundline(screen, BLACK, pos, lastpos, 3) # interpolate line
                lastpos = pos # keep track of last pos
            elif event.type == pygame.KEYDOWN: # check if key down
                if event.key == pygame.K_c: # handle clear key
                    clear_screen() # clear screen
                    score = 0 # reset score
                    qints = bqints.copy() # reset xints from backup
                    xlist = [] # reset xlist
                    poslist = [] # reset poslist
                elif event.key == pygame.K_v: # handle submission
                    xlist = sorted(xlist)
                    for xlistnum in range(1,len(xlist)): # check for discontinuities
                        if xlist[xlistnum] - xlist[xlistnum - 1] > 1: # check if discontinuous
                            score = -2000 # disqualified
                            print("discontinuous")
                    
                    hashigh = False
                    haslow = False
                    for item in poslist:
                        if item[1] < 150: # check for high point
                            hashigh = True
                        if item[1] > 400:
                            haslow = True
                    if not (hashigh or haslow): # no high point
                        score = -1000 # disqualified
                        print("filthy cheater")
                        
                        
                    if score == currentLevel + 1: # if got full points
                        globalscore += score
                        if not characterX == 12: # check not fighting bonus enemy
                            enemies[currentLevel][1] = -2 # remove enemy
                        if currentLevel == 3:
                            bonusenemy[1] = -2 # remove enemy
                        qtext, bqints = generate_factorised(5,currentLevel+2) # new harder question
                        qints = bqints.copy() # copy xintercept
                        question = graphingFont.render(qtext, True, RED) # redraw question
                        xlist = [] # reset xlist
                        poslist = [] # reset poslist
                        score = 0 # reset score
                        graphing = False # back to RPG
                        currentDialogue = ("The thug runs away in shame after losing...", None) # new dialogue
                        moveDirection = None # cancel inbound move
                        moveFrame = 0 # cancel moveframe
                        updateRPG() # display RPG
                    else: # otherwise you failed
                        qtext, bqints = generate_factorised(5,currentLevel+1) # new question
                        qints = bqints.copy() # copy xintercept
                        question = graphingFont.render(qtext, True, RED) # draw question
                        score = 0 # reset score
                        xlist = [] # reset xlist
                        poslist = [] # reset poslist
                        graphing = False # back to RPG
                        currentDialogue = ("You feel a deep shame knowing you lost.", None) # new dialogue
                        moveDirection = None # cancel move
                        moveFrame = 0 # cancel moveframe
                        updateRPG() # display RPG
                        
    if graphing or tutorial: # shortcircuit render loop to avoid movement handling code
        clock.tick(30) # render game at 30fps
        pygame.display.flip() # draw any changes to the screen
        continue
    
    # based on https://stackoverflow.com/questions/25494726/how-to-use-pygame-keydown but modified
    pressed = pygame.key.get_pressed() # handle keypress
    if pressed[pygame.K_w]:
        moveDirection = "w" # set movedirection
    elif pressed[pygame.K_s]:
        moveDirection = "s"
    elif pressed[pygame.K_a]:
        moveDirection = "a"
    elif pressed[pygame.K_d]:
        moveDirection = "d"
            
    if moveDirection: # check if moving
        if moveDirection == "w": # change sprites to animate
            if moveFrame <= 5: # switch sprites based on frame
                spriteNumber = 10 # change sprite
            else:
                spriteNumber = 6 # other sprite
        elif moveDirection == "s": # same
            if moveFrame <= 5:
                spriteNumber = 8
            else:
                spriteNumber = 4
        elif moveDirection == "a": # same
            if moveFrame <= 5:
                spriteNumber = 11
            else:
                spriteNumber = 3
        elif moveDirection == "d": # same
            if moveFrame <= 5:
                spriteNumber = 5
            else:
                spriteNumber = 1
                
        if moveFrame == 10: # check if animation has finalized
            if moveDirection == "w":
                characterY -= 1 # perform movement
                spriteNumber = 2
            elif moveDirection == "s":
                characterY += 1 # perform movement
                spriteNumber = 0
            elif moveDirection == "a":
                characterX -= 1 # perform movement
            elif moveDirection == "d":
                characterX += 1 # perform movement
                
        if currentLevel == 4 and characterX == 15: # check if the player has won the game
            gameOn = False # finish game
                
        updateRPG() # rerender
        moveFrame += 1 # next animation frame
        
        if moveFrame > 10: # check if animation has ended
            moveDirection = None # finalize move post-render
            moveFrame = 0 # reset back to first animation frame

    clock.tick(30) # render game at 30fps
    pygame.display.flip() # draw any changes to the screen
    
while True: # new gameloop
    for event in pygame.event.get(): # handle events
        if event.type == pygame.QUIT: # handle quit
            pygame.quit() # exit game
            sys.exit() # exit console
    # display ending
    screen.blit(pygame.transform.scale(pygame.image.load("game_assets/end.png"), (870,512)), (-179,0))
    pygame.display.flip() # render

