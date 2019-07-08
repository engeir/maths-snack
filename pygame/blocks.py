import pygame as pg
RED = (180, 50, 10)


class Block:
    """Make a block that have size, mass and that can collide in the horizontal plane."""
    def __init__(self, x, m, w, v):
        self.x = x
        self.m = m
        self.w = w
        self.v = -v

    def move(self):
        self.x += self.v

    def draw(self, screen, type):
        if type == 'small':
            if self.x > 150:
                pg.draw.rect(screen, RED, (self.x, 700 - self.w, self.w, self.w))
            else:
                pg.draw.rect(screen, RED, (150, 700 - self.w, self.w, self.w))
        elif type == 'big':
            if self.x > 180:
                pg.draw.rect(
                    screen, RED, (self.x, 700 - self.w, self.w, self.w))
            else:
                pg.draw.rect(screen, RED, (180, 700 - self.w, self.w, self.w))

    def coll(self):
        if self.x <= 150:
            self.v = abs(self.v)
