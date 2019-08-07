import pygame as pg

# CONSTANTS
pg.display.init()
a = pg.display.list_modes()
SCREEN_WIDTH, SCREEN_HEIGHT = a[0][0], a[0][1]
# SCREEN_WIDTH, SCREEN_HEIGHT = pg.display.Info().current_w, pg.display.Info().current_h - 50
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (20, 2, 2)
# TREE_COLOR = (20, 170, 4)

SCALING = 0.07
TWIST = 1
LENGTH = 200
GROW_SPEED = 0.01
