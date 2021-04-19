import pygame as pg
import sys, math
from random import randint
from pygame.locals import *

pg.init()

W = 1000
HW = W // 2
S = pg.display.set_mode((W, W))
CLOCK = pg.time.Clock()

BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (100, 255, 100)
color_generator = lambda: [(randint(100, 255)) for _ in range(3)]
BG = BLACK

class Circles:
    def __init__(self, radius, vel_x, vel_y, color):
        self.x = randint(radius, W - radius)
        self.y = randint(radius, W - radius)
        self.radius = radius
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.color = color

    def create(self): pg.draw.circle(S, self.color, (self.x, self.y), self.radius)

    def move_ai(self):
        if self.x + self.radius > W or self.x < 0: self.vel_x = -self.vel_x
        if self.y + self.radius > W or self.y < 0: self.vel_y = -self.vel_y

        self.x += self.vel_x
        self.y += self.vel_y


class Food:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def add(self): food_list.append(
        (randint(self.radius, W - self.radius), randint(self.radius, W - self.radius), self.color))


my_circle_x, my_circle_y, my_radius, my_speed = HW, HW, 10, 2

ai_circle_x, ai_circle_y, ai_radius, ai_vel_x, ai_vel_y = 100, 100, 10, 1, 1
ai_circle_list = [Circles(ai_radius, ai_vel_x, ai_vel_y, color_generator()) for _ in range(10)]

food_radius = 2
food_list = []
for _ in range(40):
    food = Food(randint(food_radius, W - food_radius), randint(food_radius, W - food_radius), food_radius,
                color_generator())
    food.add()

while True:
    S.fill(BLACK)
    pg.display.set_caption(f'SIZE: {round(my_radius, 2)}')
    mouse_x, mouse_y = pg.mouse.get_pos()

    if my_circle_x > mouse_x: my_circle_x -= my_speed
    if my_circle_x < mouse_x: my_circle_x += my_speed
    if my_circle_y > mouse_y: my_circle_y -= my_speed
    if my_circle_y < mouse_y: my_circle_y += my_speed

    for food in food_list:
        food_x, food_y, food_color = food
        # CALC DIST FOOD FOR PLAYER
        dist_player = math.hypot(food_x - my_circle_x, food_y - my_circle_y)
        if dist_player <= my_radius + food_radius and food in food_list:
            food_list.pop(food_list.index(food))
            my_radius += 0.1
            if my_speed > 0.07: my_speed -= 0.01
            new_food = Food(randint(food_radius, W - food_radius), randint(food_radius, W - food_radius), food_radius,
                            color_generator())
            new_food.add()

        # CALC DIST FOOD FOR AI
        for ai_circle in ai_circle_list:
            dist_ai = math.hypot(food_x - ai_circle.x, food_y - ai_circle.y)
            if dist_ai <= ai_circle.radius + food_radius and food in food_list:
                food_list.pop(food_list.index(food))
                ai_circle.radius += 1.2
                if ai_circle.vel_x > 0.07: ai_circle.vel_x -= 0.001
                if ai_circle.vel_y > 0.07: ai_circle.vel_y -= 0.001
                new_food = Food(randint(food_radius, W - food_radius), randint(food_radius, W - food_radius),
                                food_radius, color_generator())
                new_food.add()

        pg.draw.circle(S, food_color, (food_x, food_y), food_radius)

    for ai_circle in ai_circle_list:
        ai_circle.create()
        ai_circle.move_ai()

        # CALC DIST FROM PLAYER TO AI
        dist_from_circle = math.hypot(ai_circle.x - my_circle_x, ai_circle.y - my_circle_y)
        if dist_from_circle <= ai_circle.radius - my_radius:
            print("GAME OVER!")
            pg.quit()
            sys.exit()
        if dist_from_circle <= my_radius - ai_circle.radius:
            ai_circle_list.pop(ai_circle_list.index(ai_circle))
            my_radius += ai_circle.radius

        # ***** BUG *****
        # CALC DIST FROM AI TO AI
        # dist_from_other_ai = math.hypot(ai_circle.x - ai_circle_list[ai_circle_list.index(ai_circle) - 1].x, ai_circle.y - ai_circle_list[ai_circle_list.index(ai_circle) - 1].y)
        # if dist_from_other_ai <= ai_circle.radius - ai_circle_list[ai_circle_list.index(ai_circle) - 1].radius: ai_circle_list.pop(ai_circle_list.index(ai_circle)-1)
        # if dist_from_other_ai <= ai_circle_list[ai_circle_list.index(ai_circle) - 1].radius - ai_circle.radius: ai_circle_list.pop(ai_circle_list.index(ai_circle))

    pg.draw.circle(S, WHITE, (my_circle_x, my_circle_y), my_radius)

    for e in pg.event.get():
        if e.type == QUIT or len(ai_circle_list) == 0:
            print('WIN!')
            pg.quit()
            sys.exit()
    pg.display.update()
    CLOCK.tick(100)



# Todo 5: make the circles eat each other when other is larger
# calc the dist between a circle from yours
# if a circle is larger than the other & the radius of the smaller circle is fully inside the larger one...
#            ...pop the smaller & increase the radius of larger circle
# calc the dist between a circle from another circle, DUNNO HOW TO DO THIS YET...
# just refine some vars
# *** THIS IS IT FOR NOW! ***

# Todo 4: create the other AI circles
# in the Circles 'create' method,
# make pg spawn a circle in a random pos w/ its attributes (just one ai circle for now)
# add the ai circle into a list
# make the ai circles move, they'll move straight but bounces back at the screen borders
# calc the dist between an ai circle & a food... WHERE SHOULD I PUT THE CODE? in the loop where we create food
#   - i think we're gonna use a nested for loop for this, cz each list has a diff # of things...
#   - and for each of those things we calc the dist between ALL of the other things
# when an ai circle touches a food it disappears then circle grows & speed decreases slightly

# Todo 3:
# when circle touches food increase its size & slightly decrease it's speed
# when u eat a food, a new food will be created in a new random pos
# rewrite into the switch-case statement
# ** I'VE JUST FOUND OUT THAT THERE'S NO SWITCH-CASE IN PY! **

# Todo 2:
# create a Food class w/ a that creates a small circle "IS THIS NECESSARY?"...
#   - maybe just a for loop'd be fine instead
# find out a way to access the coords of each of the foods: a for loop
# when your circle touches a food it pop it out the list & increase your radius
# ** A BUG OCCURRED **: THE FOOD KEEPS SPAWNING, so i'll make a Food class!
#   - then make a boolean switch when circle touches food to prevent the bug
# ** A BUG OCCURRED **: THE FOOD THAT I COLLIDED W/ DIDNT DISAPPEAR, cz you're not popping that specific food!
#   - when u eat a food, its random & when u pop() it pops it in order until the food you're touching is popped!
#   - seemed like i didnt need the boolean switch after all!, simply find the index of the touched food then pop it!
# **** BUGS SOLVED ****

# Todo 1:
# u don't need a class for your own circle YET cz its just 1!
# define the vars for your own circle
# get the pos of the mouse & assign vars for it
# make your circle follow the mouse
