import config as cf
import numpy as np
import pygame as pg


class TimesTable:
    """Make a times table calculation."""

    def __init__(self, points):
        self.points = points
        self.radius = cf.RADIUS

    def draw(self, screen, factor, pt):
        pg.draw.circle(
            screen,
            cf.WHITE,
            (int(cf.SCREEN_WIDTH / 2), int(cf.SCREEN_HEIGHT / 2)),
            self.radius,
            1,
        )
        for i in range(pt):
            angle = 2 * np.pi * i / pt
            x = int(self.radius * np.cos(angle) + cf.SCREEN_WIDTH / 2)
            y = int(self.radius * np.sin(angle) + cf.SCREEN_HEIGHT / 2)
            i_ = i * factor % pt
            angle_ = 2 * np.pi * i_ / pt
            x_ = int(self.radius * np.cos(angle_) + cf.SCREEN_WIDTH / 2)
            y_ = int(self.radius * np.sin(angle_) + cf.SCREEN_HEIGHT / 2)
            pg.draw.circle(screen, cf.WHITE, (x, y), 3, 0)
            pg.draw.line(screen, cf.WHITE, (x, y), (x_, y_), 1)
