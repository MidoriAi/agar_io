

import pygame as pg
import sys, random
from pygame.locals import *

pg.init()

W = 500
HW = W//2
s = pg.display.set_mode((W, W))
CLOCK = pg.time.Clock()

BLACK = (50, 50, 50)
WHITE = (255, 255, 255)

radius = 10
circle_x = radius

bg = pg.image.load('hex_smooth_gray.jpg').convert()
bg_width, bg_height = bg.get_rect().size

stage_width = bg_width
stage_x = 0
start_scroll_x = HW

player_x = radius
player_y = HW
player_vel_x = 0

class Circle:
    def __init__(self, x, y, radius, speed=5):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel_x = 0
        self.vel_y = 0
        self.speed = speed
        self.circle_x = self.radius
        self.player_x = self.radius
        self.player_y = HW
        self.player_vel_x = 0

    def create_circle(self): pg.draw.circle(s, WHITE, (self.circle_x, self.player_y - self.radius), self.radius)

    def move(self):
        global stage_x
        keys = pg.key.get_pressed()
        if keys[K_RIGHT]: self.player_vel_x = self.speed
        elif keys[K_LEFT]: self.player_vel_x = -self.speed
        else: self.player_vel_x = 0
        self.player_x += self.player_vel_x

        if self.player_x > stage_width - self.radius: self.player_x = stage_width - self.radius
        if self.player_x < self.radius: self.player_x = self.radius

        if self.player_x < start_scroll_x: self.circle_x = self.player_x
        elif self.player_x > stage_width - start_scroll_x: self.circle_x = self.player_x - stage_width + W
        else:
            self.circle_x = start_scroll_x
            stage_x += -self.player_vel_x

        rel_x = stage_x % bg_width
        s.blit(bg, (rel_x - bg_width, 0))
        if rel_x < W: s.blit(bg, (rel_x, 0))

        self.create_circle()

my_circle = Circle(circle_x, HW, radius)

while True:
    s.fill(BLACK)
    my_circle.move()

    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()
    CLOCK.tick(60)

# Todo 2 -- MAKE THE SCROLL EFFECT --
# dunno what the steps are ... :/ 😣

# Todo 1 -- DISPLAY THE 1st CIRCLE AND MAKE IT MOVE THRU X AXIS--
# make a class for Circle w/ create(), move() methods