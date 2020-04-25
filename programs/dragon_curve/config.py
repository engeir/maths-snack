import pygame as pg

# CONSTANTS

# Display
pg.display.init()
# a = pg.display.list_modes()
# SCREEN_WIDTH, SCREEN_HEIGHT = a[0][0], a[0][1]
a = pg.display.set_mode((0, 0))
SCREEN_WIDTH, SCREEN_HEIGHT = a.get_clip()[2], a.get_clip()[3]
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

x_0, y_0 = int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)

START = [
    [x_0, x_0, y_0, y_0 - 1],
    [x_0, x_0 + 2, y_0, y_0],
    [x_0 - 5, x_0, y_0, y_0],
    [x_0, x_0, y_0 - 40, y_0]
]
