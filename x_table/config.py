import pygame as pg

# CONSTANTS
# SCREEN_WIDTH = 900
# SCREEN_HEIGHT = SCREEN_WIDTH
pg.display.init()
a = pg.display.list_modes()
SCREEN_WIDTH, SCREEN_HEIGHT = a[0][0], a[0][1]
# SCREEN_WIDTH, SCREEN_HEIGHT = pg.display.Info().current_w, pg.display.Info().current_h
FPS = 30

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (20, 2, 2)
GREEN = (20, 170, 4)
RED = (200, 10, 10)

RADIUS = 500  # int(SCREEN_WIDTH / 2 - 60)
