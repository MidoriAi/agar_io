import pygame as pg
import sys, random, math
from pygame.locals import *

pg.init()

W = 800
HW = W//2
S = pg.display.set_mode((W, W))
CLOCK = pg.time.Clock()

BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (100, 255, 100)

class Circles:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

    def create(self):
        pass

    def move(self):
        pass


my_circle_x, my_circle_y, my_radius = HW, HW, 10

while True:
    S.fill(BLACK)

    mouse_x, mouse_y = pg.mouse.get_pos()

    if my_circle_x > mouse_x: my_circle_x -= 1
    if my_circle_x < mouse_x: my_circle_x += 1
    if my_circle_y > mouse_y: my_circle_y -= 1
    if my_circle_y < mouse_y: my_circle_y += 1

    pg.draw.circle(S, WHITE, (my_circle_x, my_circle_y), my_radius)

    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()
    CLOCK.tick(100)


# Todo 2:
#

# Todo 1:
# u don't need a class for your own circle YET cz its just 1!
# define the vars for your own circle
# get the pos of the mouse & assign vars for it
# make your circle follow the mouse