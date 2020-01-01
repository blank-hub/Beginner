import pygame
import sys
import time
from pygame.locals import *
from random import randint

balls = []
booms = []
foods = []

r1 = (200, 50, 50)
w = 255, 255, 255
g = (50, 200, 50)
b = (0, 0, 0)
blue = (50, 50, 200)
yellow = (230, 230, 50)
long = 1200
wide = 800
purple = 100, 0, 205

pygame.init()
screen = pygame.display.set_mode((long, wide))
pygame.display.set_caption('Ball Eating Game')
font1 = pygame.font.Font(None, 45)
game_over = True
v = 15
flag = 0


def random_color():
    re = randint(0, 255)
    gr = randint(0, 255)
    bl = randint(0, 255)
    return re, gr, bl


class Food(object):
    def __init__(self):
        self.x = randint(0, long)
        self.y = randint(0, wide)
        self.color = purple
        self.r = randint(5, 9)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


class Ball(object):
    def __init__(self, x, y, vx, vy, r, colour, alive=True):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.colour = colour
        self.alive = alive

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0 or self.x > long:
            self.x = long-self.x

        if self.y < 0 or self.y > wide:
            self.y = wide-self.y
        if self.r < 10:
            self.alive = False

    def eat(self, other):
        if self.alive:
            dx, dy = self.x-other.x, self.y-other.y
            distance = (dx**2+dy**2)**0.5
            if distance < self.r and other != self:
                self.r += other.r*0.2
                if other in foods:
                    foods.remove(other)
                elif other in balls and self != other:
                    other.alive = False

    def boom(self):
        if self.r > 11:
            self.r -= self.r*0.1
            boom_x, boom_y = self.x+int(self.r)+10, self.y+int(self.r)+10
            boom_vx, boom_vy = self.vx, self.vy
            bom = Boom(boom_x, boom_y, boom_vx, boom_vy, r=10, colour=r1)
            booms.append(bom)

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), int(self.r))
        #screen.blit(image, (self.x, self.y))


class Boom(object):
    def __init__(self, x, y, vx, vy, r, colour=r1, alive=True):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.colour = colour
        self.alive = alive

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0 or self.x > long:
            self.x = long-self.x

        if self.y < 0 or self.y > wide:
            self.y = wide-self.y

    def bang(self, others):
        xx = others.x
        yy = others.y
        rr = others.r
        dis = ((self.x-xx)**2+(self.y-yy)**2)**0.5
        if dis <= rr and self != others:
            others.r -= 5
            others.colour = random_color()
            if others.r < 5:
                others.alive = False
            booms.remove(self)

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), int(self.r))


def print_txt(font, x, y, txt):
    image = font.render(txt, True, r1)
    screen.blit(image, (x, y))


while True:

    if flag == 0:
        ball1 = Ball(randint(0, 800), randint(0, 600), 0, 0, 30, colour=random_color())
        ball2 = Ball(randint(0, 800), randint(0, 600), 0, 0, 30, colour=random_color())
        balls.append(ball1)
        balls.append(ball2)
        flag = 1
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                game_over = False
                t1 = time.time()
                t2 = time.time()

    background = pygame.image.load('ball1.jpg').convert_alpha()
    screen.blit(background, (0, 0))
    image = pygame.image.load('feidie.jpg')

    if not game_over:
        pygame.key.get_repeat()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        if keys[K_w]:
            ball1.vy = -v
            ball1.vx = 0
        if keys[K_s]:
            ball1.vy = v
            ball1.vx = 0
        if keys[K_d]:
            ball1.vx = v
            ball1.vy = 0
        if keys[K_a]:
            ball1.vx = -v
            ball1.vy = 0
        if keys[K_UP]:
            ball2.vy = -v
            ball2.vx = 0
        if keys[K_DOWN]:
            ball2.vy = v
            ball2.vx = 0
        if keys[K_LEFT]:
            ball2.vx = -v
            ball2.vy = 0
        if keys[K_RIGHT]:
            ball2.vx = v
            ball2.vy = 0
        if keys[K_h]:
            if time.time() - t1 > 0.5:
                ball1.boom()
                t1 = time.time()
        if keys[K_SPACE]:
            if time.time() - t2 > 0.5:
                ball2.boom()
                t2 = time.time()

        if not keys[K_w] and not keys[K_s] and not keys[K_a] and not keys[K_d]:
            ball1.vx = 0
            ball1.vy = 0
        if not keys[K_UP] and not keys[K_DOWN] and not keys[K_LEFT] and not keys[K_RIGHT]:
            ball2.vx = 0
            ball2.vy = 0

        if int(time.time()) % 2 == 1:
            foo = Food()
            foods.append(foo)

        for ball in balls:
            if ball.alive:
                ball.draw()
            else:
                balls.remove(ball)

        #pygame.display.flip()
        pygame.time.delay(10)
        for i in foods:
            i.draw()
        for ball in balls:
            ball.move()
            for oth in foods:
                ball.eat(oth)
            for o in balls:
                ball.eat(o)
        for boom in booms:
            boom.move()
            boom.draw()
            for i in balls:
                boom.bang(i)

        if not ball1.alive:
            print_txt(font1, 100, 300, 'GAME OVER!  2 WINS!')
            pygame.time.delay(20)
            game_over = True
            flag -= 1
            balls.remove(ball2)
            booms = []
        elif not ball2.alive:
            print_txt(font1, 100, 300, 'GAME OVER!  1 WINS')
            pygame.time.delay(20)
            game_over = True
            flag -= 1
            balls.remove(ball1)
            booms = []

        if game_over:
            print_txt(font1, 100, 400, 'Plz click to begin')

        pygame.display.update()