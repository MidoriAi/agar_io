import pygame as pg
import sys, math
from pygame.locals import *

pg.init()

W = 500
HW = W//2
S = pg.display.set_mode((W, W))
CLOCK = pg.time.Clock()

BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (100, 255, 100)

x1, y1, radius1, color1 = None, None, 20, WHITE
x2, y2, radius2, color2 = HW, HW, 50, GREEN

while True:
    S.fill(BLACK)

    mouse_x, mouse_y = pg.mouse.get_pos()
    x1, y1 = mouse_x, mouse_y

    dist = math.hypot(x1 - x2, y1 -y2)
    if dist <= radius1 + radius2: color2 = RED
    else: color2 = GREEN

    pg.draw.circle(S, color2, (x2, y2), radius2)
    pg.draw.circle(S, color1, (x1, y1), radius1)

    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()
    CLOCK.tick(60)


# Todo 2:
# to get the dist_player of the circles from each other, use 'math.hypot(x1 - x2, y1 - y2)'
# test the collision by adding the circles' radiuses & comparing it w/ the dist_player...
#   - if dist_player <= radius1 + radius2 ,then a collision has occurred
# finally, draw the circles into the display

# Todo 1:
# define the vars for 2 circles, 1st circle will be controlled by your mouse & the 2nd is static/dynamic
# get the coords of the mouse & store it to vars