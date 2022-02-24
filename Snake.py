import pygame
import random
from pygame.locals import*
pygame.init()
pygame.display.set_caption('Snake')
run = True
pos = (0, 0)
game = True
score = 0
size = 20
best = 0
menu = True
width = size*35
height = size*35
applex = size * random.randint(2, 32)
appley = size * random.randint(3, 32)
down = False
up = False
right = False
left = False
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
clock = pygame.time.Clock()
parts = []
font = pygame.font.Font('freesansbold.ttf', 32)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
appleColor = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))
snakeColor = white


class Part:
    def __init__(part, number, posx, posy):
        part.number = number
        part.posx = posx
        part.posy = posy


parts = []
parts.append(Part(0, size*6, size*6))


def Events():
    global left
    global right
    global up
    global down
    global run
    global menu
    global game
    global pos
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
            game = False
            menu = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP and down == False:
                up = True
                right = False
                left = False
            if event.key == K_LEFT and right == False:
                left = True
                down = False
                up = False
            if event.key == K_DOWN and up == False:
                down = True
                right = False
                left = False
            if event.key == K_RIGHT and left == False:
                right = True
                down = False
                up = False


def Field():
    for i in range(1, 34):
        for j in range(2, 34):
            if i % 2 == j % 2:
                pygame.draw.rect(screen, (30, 30, 30),
                                 pygame.Rect(i*size, j*size, size, size))
            else:
                pygame.draw.rect(screen, (40, 40, 40),
                                 pygame.Rect(i*size, j*size, size, size))
    
while run:
    menu = True
    run = True
    pos = (0, 0)
    game = True
    score = 0
    down = False
    up = False
    right = False
    left = False
    parts = []
    snakeColor = white
    parts = []
    parts.append(Part(0, size*6, size*6))
    while menu:
        screen.fill(black)
        text = font.render('Best: ' + str(best), True, white, black)
        play = font.render('Play', True, white, black)
        textRect = text.get_rect()
        playRect = play.get_rect()
        textRect.center = (width/2, size*2)
        playRect.center = (width/2, size*10)
        screen.blit(text, textRect)
        screen.blit(play, playRect)
        Events()
        if playRect.collidepoint(pos):
            menu = False
            game = True       
        pygame.display.update()
        
    while game:
        screen.fill(black)
        Field()
        text = font.render('Score: ' + str(score) + str(' ')*40 +'Best: ' + str(best), True, white, black)
        textRect = text.get_rect()
        textRect.center = (width/2, size)
        screen.blit(text, textRect)
        clock.tick(12)
        Events()
        for i in reversed(parts):
            if i == parts[0]:
                if i.posx == applex and i.posy == appley:
                    parts.append(Part(len(parts), parts[-1].posx, parts[-1].posy))
                    score += 1
                    if best < score:
                        best = score
                    applex = size * random.randint(2, 32)
                    appley = size * random.randint(3, 32)
                    snakeColor = appleColor
                    appleColor = (random.randint(0, 255), random.randint(
                        0, 255), random.randint(0, 255))
                if up == True:
                    i.posy -= size
                if down == True:
                    i.posy += size
                if left == True:
                    i.posx -= size
                if right == True:
                    i.posx += size
                if i.posx > width - size*2 or i.posx < size:
                    game = False
                elif i.posy > height - size*2 or i.posy < size*2:
                    game = False
            else:
                i.posx = parts[i.number - 1].posx
                i.posy = parts[i.number - 1].posy
        for i in parts:
            if i != parts[0] and parts[0].posx == i.posx and parts[0].posy == i.posy:
                game = False
        for i in parts:
            if game == True:
                pygame.draw.rect(screen, snakeColor, pygame.Rect(
                    i.posx, i.posy, size, size))
        pygame.draw.rect(screen, appleColor, pygame.Rect(
            applex, appley, size, size))
        pygame.display.update()
