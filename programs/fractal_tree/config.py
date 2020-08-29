import pygame as pg

# CONSTANTS
pg.display.init()
# a = pg.display.list_modes()
# SCREEN_WIDTH, SCREEN_HEIGHT = a[0][0], a[0][1]
a = pg.display.set_mode((0, 0))
SCREEN_WIDTH, SCREEN_HEIGHT = a.get_clip()[2], a.get_clip()[3]
# SCREEN_WIDTH, SCREEN_HEIGHT = pg.display.Info().current_w, pg.display.Info().current_h - 50
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (20, 2, 2)
# TREE_COLOR = (20, 170, 4)

# SCALING = 0.07
SCALING = 0.9
TWIST = 1
LENGTH = SCREEN_HEIGHT * .12
# LENGTH = 400
GROW_SPEED = 0.05  # 0.01
