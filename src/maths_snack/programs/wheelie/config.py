import itertools

import numpy as np
import pygame as pg

# CONSTANTS
# SCREEN_WIDTH = 900
# SCREEN_HEIGHT = SCREEN_WIDTH
pg.display.init()
a = pg.display.set_mode((0, 0))
# print(screeen.get_clip()[2])
# a = pg.display.list_modes()
# SCREEN_WIDTH, SCREEN_HEIGHT = a[0][0], a[0][1]
SCREEN_WIDTH, SCREEN_HEIGHT = int(a.get_clip()[2]), int(a.get_clip()[3])  # * .96)
# SCREEN_WIDTH, SCREEN_HEIGHT = pg.display.Info().current_w, pg.display.Info().current_h
FPS = 30

TXT_BIG = int(SCREEN_WIDTH * 0.03)
TXT_SMALL = int(SCREEN_WIDTH * 0.018)

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (20, 2, 2)
GREEN = (20, 170, 4)
RED = (200, 10, 10)
R1 = (255, 0, 0)
R2 = (255, 127, 0)
R3 = (255, 255, 0)
R4 = (0, 255, 0)
R5 = (0, 0, 255)
R6 = (75, 0, 130)
R7 = (143, 0, 255)
RAINBOWnp = np.array([])
RAINBOWnp = np.r_[
    [
        [x, y, z]
        for x, y, z in np.linspace(
            start=[R1[0], R1[1], R1[2]], stop=[R2[0], R2[1], R2[2]], num=10
        )
    ]
]
RAINBOWnp = np.r_[
    RAINBOWnp,
    [
        [x, y, z]
        for x, y, z in np.linspace(
            start=[R2[0], R2[1], R2[2]], stop=[R3[0], R3[1], R3[2]], num=10
        )
    ],
]
RAINBOWnp = np.r_[
    RAINBOWnp,
    [
        [x, y, z]
        for x, y, z in np.linspace(
            start=[R3[0], R3[1], R3[2]], stop=[R4[0], R4[1], R4[2]], num=10
        )
    ],
]
RAINBOWnp = np.r_[
    RAINBOWnp,
    [
        [x, y, z]
        for x, y, z in np.linspace(
            start=[R4[0], R4[1], R4[2]], stop=[R5[0], R5[1], R5[2]], num=10
        )
    ],
]
RAINBOWnp = np.r_[
    RAINBOWnp,
    [
        [x, y, z]
        for x, y, z in np.linspace(
            start=[R5[0], R5[1], R5[2]], stop=[R6[0], R6[1], R6[2]], num=10
        )
    ],
]
RAINBOWnp = np.r_[
    RAINBOWnp,
    [
        [x, y, z]
        for x, y, z in np.linspace(
            start=[R6[0], R6[1], R6[2]], stop=[R7[0], R7[1], R7[2]], num=10
        )
    ],
]
RAINBOWnp = np.r_[
    RAINBOWnp,
    [
        [x, y, z]
        for x, y, z in np.linspace(
            start=[R7[0], R7[1], R7[2]], stop=[R1[0], R1[1], R1[2]], num=10
        )
    ],
]
RAINBOW = itertools.cycle(RAINBOWnp)

# RADIUS = int(SCREEN_HEIGHT / 2 - SCREEN_HEIGHT * .1)  # 500
RADIUS = int(SCREEN_WIDTH / 4 - SCREEN_WIDTH * 0.01)  # 500
