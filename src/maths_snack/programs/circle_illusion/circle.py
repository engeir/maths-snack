import config as cf
import numpy as np
import pygame as pg


class Circle:
    """Make a times table calculation."""

    def __init__(self, points):
        self.points = points
        self.radius = cf.RADIUS

    def draw(self, screen, factor, pt, lines, circle):
        if circle:
            pg.draw.circle(
                screen,
                cf.WHITE,
                (int(cf.SCREEN_WIDTH / 2), int(cf.SCREEN_HEIGHT / 2)),
                self.radius,
                1,
            )
        for i in range(pt):
            angle = np.pi * i / pt
            x0 = int(self.radius * np.cos(angle) + cf.SCREEN_WIDTH / 2)
            y0 = int(self.radius * np.sin(angle) + cf.SCREEN_HEIGHT / 2)
            angle_ = np.pi * i / pt + np.pi
            x1 = int(self.radius * np.cos(angle_) + cf.SCREEN_WIDTH / 2)
            y1 = int(self.radius * np.sin(angle_) + cf.SCREEN_HEIGHT / 2)
            x_ = (x1 - x0) * (0.5 + np.cos(angle + factor) / 2) + x0
            y_ = (y1 - y0) * (0.5 + np.cos(angle + factor) / 2) + y0
            pg.draw.circle(screen, cf.WHITE, (x_, y_), 4, 0)
            if lines:
                pg.draw.line(screen, cf.RED, (x0, y0), (x1, y1), 1)
