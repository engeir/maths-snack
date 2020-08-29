import numpy as np
import pygame as pg
import config as cf


class Tree:
    """Make a times table calculation."""

    def __init__(self):
        self.last_gen_start = [(cf.SCREEN_WIDTH / 2, cf.SCREEN_HEIGHT - cf.SCREEN_HEIGHT * .1)]
        self.last_gen_stop = [(cf.SCREEN_WIDTH / 2, cf.SCREEN_HEIGHT - (cf.LENGTH + 100))]
        # self.last_gen_start = [(cf.SCREEN_WIDTH / 2, cf.SCREEN_HEIGHT / 2)]
        # self.last_gen_stop = [(cf.SCREEN_WIDTH / 2, cf.SCREEN_HEIGHT / 2 - 1)]
        self.scale = 1
        self.repr_nr = 3
        self.twist_div = 20  # Sierpinski: 120
        self.twist = np.pi * self.twist_div / 180
        self.r = 173  # 139
        self.g = 255  # 69
        self.b = 47  # 19

    def draw(self, screen, generation, grow):
        # Nvm this, just colouring in
        if int(139 + 3.4 * generation) <= 255:
            self.r = int(139 + 3.4 * generation)
        if int(69 + 18.6 * generation) <= 255:
            self.g = int(69 + 18.6 * generation)
        if int(19 + 2.8 * generation) <= 255:
            self.b = int(19 + 2.8 * generation)
        if 5 - np.log(3 * generation + 1) > 0.9:
            width = int(5 - np.log(3 * generation + 1))
        else:
            width = 1
        for start, stop in zip(self.last_gen_start, self.last_gen_stop):
            stop = (stop[0] - (stop[0] - start[0]) * (1 - grow), stop [1] - (stop[1] - start[1]) * (1 - grow))
            pg.draw.line(screen, (self.r, self.g, self.b), start, stop, width)

    def structure(self, generation):
        self.scale *= cf.SCALING
        # if self.twist_div - cf.TWIST > 2.2:
        #     self.twist_div -= cf.TWIST
        #     self.twist = np.pi / self.twist_div
        branches = self.repr_nr**generation
        past_start = np.copy(self.last_gen_start)
        past_stop = np.copy(self.last_gen_stop)
        self.last_gen_start = [x for x in self.last_gen_stop for _ in range(self.repr_nr)]
        self.last_gen_stop = np.copy(self.last_gen_start)
        for branch in range(branches):
            direction = past_stop[branch][0] - past_start[branch][0] + \
                (past_stop[branch][1] - past_start[branch][1]) * 1j
            for child in range(self.repr_nr):
                direction_ = direction * np.exp(self.twist * (child - (self.repr_nr / 2 - .5)) * 1j)
                direction_ /= np.abs(direction_)
                self.last_gen_stop[self.repr_nr * branch + child] = (past_stop[branch][0] + np.real(direction_) * cf.LENGTH * self.scale,
                                                                     past_stop[branch][1] + np.imag(direction_) * cf.LENGTH * self.scale)
            # direction_1 = direction * np.exp(self.twist * 1j)
            # direction_2 = direction * np.exp(- self.twist * 1j)
            # direction_3 = direction * np.exp(- self.twist * 0)
            # direction_1 /= np.abs(direction_1)
            # direction_2 /= np.abs(direction_2)
            # direction_3 /= np.abs(direction_3)
            # self.last_gen_stop[self.repr_nr * branch] = (past_stop[branch][0] + np.real(direction_1) * cf.LENGTH * self.scale,
            #                                        past_stop[branch][1] + np.imag(direction_1) * cf.LENGTH * self.scale)
            # self.last_gen_stop[self.repr_nr * branch + 1] = (past_stop[branch][0] + np.real(direction_2) * cf.LENGTH * self.scale,
            #                                            past_stop[branch][1] + np.imag(direction_2) * cf.LENGTH * self.scale)
            # self.last_gen_stop[self.repr_nr * branch + 2] = (past_stop[branch][0] + np.real(direction_3) * cf.LENGTH * self.scale,
            #                                            past_stop[branch][1] + np.imag(direction_3) * cf.LENGTH * self.scale)
