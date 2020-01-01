import pygame
import sys
import time
import random
from pygame.locals import *
from random import randint


def print_txt(font, x, y, txt, color=(255, 255, 255)):
    image = font.render(txt, True, color)
    screen.blit(image, (x, y))


pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption('how fast you are')
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 80)
game_over = True
current = 0
score = 0
seconds = 11
answer = randint(97, 122)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    if keys[K_RETURN]:
        game_over = False
        score = 0
        t0 = time.time()

    if not game_over:
        current = time.time() - t0
        if seconds < current:
            game_over = True
        elif keys[answer]:
            score += 1
            answer = randint(97, 122)

    screen.fill((0, 0, 0))
    print_txt(font1, 0, 0, "Let's see how fast you can type!")
    print_txt(font1, 0, 40, 'Try to keep up for 10 seconds!')

    if not game_over:
        print_txt(font1, 0, 80, 'Time:')
        print_txt(font1, 100, 80, str(int(current)))

    if game_over:
        print_txt(font1, 0, 250, 'Plz press enter to start!')

    speed = score*6
    print_txt(font1, 0, 110, 'Speed:')
    print_txt(font1, 100, 110, str(speed))
    print_txt(font1, 160, 110, 'letters/min')
    print_txt(font2, 130, 170, str.upper(chr(answer)), (255, 0, 100))

    pygame.display.update()


