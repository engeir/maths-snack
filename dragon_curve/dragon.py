import numpy as np
import pygame as pg
import config as cf


class Dragon:
    """Make a Dragon curve."""

    def __init__(self, auto, dragon_size):
        self.auto = auto
        self.dragon_size = int(dragon_size - 1)
        self.curve = [[cf.START[self.dragon_size][0], cf.START[self.dragon_size][2]],
                      [cf.START[self.dragon_size][1], cf.START[self.dragon_size][3]]]
        self.stop = [18, 17, 16, 10]

    def structure(self):
        last_curve = np.copy(self.curve)
        new_curve = []
        for pt in last_curve:
            pt = (pt[0] - last_curve[-1][0], pt[1] - last_curve[-1][1])
            new = (pt[0] + pt[1] * 1j) * np.exp(np.pi / 2 * 1j)
            new_curve.append([np.real(new) + last_curve[-1][0],
                              np.imag(new) + last_curve[-1][1]])
        reversed_curve = new_curve[::-1]
        reversed_curve.pop(0)
        self.curve = self.curve + reversed_curve

    def draw_manual(self, screen):
        pg.draw.lines(screen, cf.WHITE, False, self.curve, 1)

    def draw_auto(self, screen, angle, dragon_tails):
        if dragon_tails > self.stop[self.dragon_size]:
            pg.draw.lines(screen, cf.WHITE, False, self.curve, 1)
        else:
            last_curve = np.copy(self.curve)
            new_curve = []
            if angle < np.pi / 2:
                for pt in last_curve:
                    pt = (pt[0] - last_curve[-1][0], pt[1] - last_curve[-1][1])
                    new = (pt[0] + pt[1] * 1j) * np.exp(angle * 1j)
                    new_curve.append([np.real(new) + last_curve[-1][0],
                                      np.imag(new) + last_curve[-1][1]])
            else:
                for pt in last_curve:
                    pt = (pt[0] - last_curve[-1][0], pt[1] - last_curve[-1][1])
                    new = (pt[0] + pt[1] * 1j) * np.exp(np.pi / 2 * 1j)
                    new_curve.append([np.real(new) + last_curve[-1][0],
                                      np.imag(new) + last_curve[-1][1]])
                reversed_curve = new_curve[::-1]
                reversed_curve.pop(0)
                self.curve = self.curve + reversed_curve
            pg.draw.lines(screen, cf.WHITE, False, self.curve, 1)
            pg.draw.lines(screen, cf.RED, False, new_curve, 1)

    def draw(self, screen, angle, dragon_tails):
        if self.auto:
            self.draw_auto(screen, angle, dragon_tails)
        else:
            self.draw_manual(screen)
