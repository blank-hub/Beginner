import pygame
import math
import sys
import random
from random import randint, shuffle
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption('PieGame')
myfont = pygame.font.Font(None, 60)

color = 255, 255, 255
width = 4
x = 380
y = 300
r = 100
pos = x-r, y-r, 2*r, 2*r

piece1 = piece2 = piece3 = piece4 = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                piece1 = True
            elif event.key == pygame.K_2:
                piece2 = True
            elif event.key == pygame.K_3:
                piece3 = True
            elif event.key == pygame.K_4:
                piece4 = True

    screen.fill((0, 0, 0))
    out = myfont.render('Welcome to piegame!', True, (255, 255, 255))
    screen.blit(out, (10, 10))

    txt1 = myfont.render('1', True, color)
    screen.blit(txt1, (x + r / 2 - 20, y - r / 2))
    txt2 = myfont.render('2', True, color)
    screen.blit(txt2, (x + r / 2 - 20, y + r / 2 - 20))
    txt3 = myfont.render('3', True, color)
    screen.blit(txt3, (x - r / 2, y + r / 2 - 20))
    txt4 = myfont.render('4', True, color)
    screen.blit(txt4, (x - r / 2, y - r / 2))

    if piece1:
        angle1 = math.radians(0)
        angle2 = math.radians(90)
        pygame.draw.arc(screen, color, pos, angle1, angle2, width)
        pygame.draw.line(screen, color, (x, y), (x, y-r), width)
        pygame.draw.line(screen, color, (x, y), (x+r, y), width)
    if piece2:
        angle1 = math.radians(270)
        angle2 = math.radians(360)
        pygame.draw.arc(screen, color, pos, angle1, angle2, width)
        pygame.draw.line(screen, color, (x, y), (x+r, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y+r), width)
    if piece3:
        angle1 = math.radians(180)
        angle2 = math.radians(270)
        pygame.draw.arc(screen, color, pos, angle1, angle2, width)
        pygame.draw.line(screen, color, (x, y), (x, y+r), width)
        pygame.draw.line(screen, color, (x, y), (x-r, y), width)
    if piece4:
        angle1 = math.radians(90)
        angle2 = math.radians(180)
        pygame.draw.arc(screen, color, pos, angle1, angle2, width)
        pygame.draw.line(screen, color, (x, y), (x, y-r), width)
        pygame.draw.line(screen, color, (x, y), (x-r, y), width)

    txt = myfont.render('YOU WIN !', True, (255, 255, 255))
    if piece1 and piece2 and piece3 and piece4:
        screen.blit(txt, (x-r+6, y+r+30))
        color = 0, 255, 0

    pygame.display.update()


