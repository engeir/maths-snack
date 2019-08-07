import pygame as pg

# CONSTANTS

# Display
pg.display.init()
a = pg.display.list_modes()
SCREEN_WIDTH, SCREEN_HEIGHT = a[0][0], a[0][1]
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (20, 2, 2)
GREEN = (20, 170, 4)
RED = (200, 10, 10)
# TREE_COLOR = (20, 170, 4)

# Dragon Curve
SCALING = 0.07
TWIST = 1
LENGTH = 10

START = [
    [900, 900, 351, 350],
    [1848, 1850, 1250, 1250],
    [700, 705, 720, 720],
    [760, 760, 605, 645]
]
