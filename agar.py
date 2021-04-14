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
def color_generator(): return [(random.randint(100, 255)) for _ in range(3)]

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

class Food:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def add(self): food_list.append((random.randint(self.radius, W - self.radius), random.randint(self.radius, W - self.radius), self.color))


my_circle_x, my_circle_y, my_radius = HW, HW, 10

food_radius = 2
food_list = []
for i in range(100):
    new_food = Food(random.randint(food_radius, W-food_radius), random.randint(food_radius, W-food_radius), food_radius, color_generator())
    new_food.add()

while True:
    S.fill(BLACK)

    mouse_x, mouse_y = pg.mouse.get_pos()

    # i'd like to make this into a switch-case statement later!
    if my_circle_x > mouse_x: my_circle_x -= 1
    if my_circle_x < mouse_x: my_circle_x += 1
    if my_circle_y > mouse_y: my_circle_y -= 1
    if my_circle_y < mouse_y: my_circle_y += 1

    for food in food_list:
        food_x, food_y, food_color = food
        dist = math.hypot(food_x - my_circle_x, food_y - my_circle_y)
        if dist <= my_radius + food_radius: food_list.pop(food_list.index(food))
        pg.draw.circle(S, food_color, (food_x, food_y), food_radius)

    pg.draw.circle(S, WHITE, (my_circle_x, my_circle_y), my_radius)

    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()
    CLOCK.tick(100)


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