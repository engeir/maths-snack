import numpy as np
import pygame as pg


class DoublePendulum:
    """Make an objects that is the simulation."""

    def __init__(self, r1, r2, m1, m2, a1, a2):
        self.x0, self.y0 = 300, 200
        self.r1, self.r2 = r1, r2
        self.m1, self.m2 = m1, m2
        self.a1, self.a2 = a1, a2
        self.a1_v, self.a2_v, self.a1_a, self.a2_a = 0, 0, 0, 0
        self.g = 10
        self.x1, self.y1, self.x2, self.y2 = 0, 0, 0, 0
        self.num1, self.num2, self.num3, self.num4 = 0, 0, 0, 0
        self.numm1, self.numm2, self.numm3, self.numm4 = 0, 0, 0, 0
        self.den, self.denn = 0, 0

    def angles(self):
        self.num1 = -self.g * (2 * self.m1 + self.m2) * np.sin(self.a1)
        self.num2 = -self.m2 * self.g * np.sin(self.a1 - 2 * self.a2)
        self.num3 = -2 * np.sin(self.a1 - self.a2) * self.m2
        self.num4 = self.a2_v ** 2 * self.r2 + self.a1_v ** 2 * self.r1 * np.cos(
            self.a1 - self.a2
        )
        self.den = self.r1 * (
            2 * self.m1 + self.m2 - self.m2 * np.cos(2 * self.a1 - 2 * self.a2)
        )
        self.a1_a = (self.num1 + self.num2 + self.num3 * self.num4) / self.den

        self.numm1 = 2 * np.sin(self.a1 - self.a2)
        self.numm2 = self.a1_v ** 2 * self.r1 * (self.m1 + self.m2)
        self.numm3 = self.g * (self.m1 + self.m2) * np.cos(self.a1)
        self.numm4 = self.a2_v ** 2 * self.r2 * self.m2 * np.cos(self.a1 - self.a2)
        self.denn = self.r2 * (
            2 * self.m1 + self.m2 - self.m2 * np.cos(2 * self.a1 - 2 * self.a2)
        )
        self.a2_a = (self.numm1 * (self.numm2 + self.numm3 + self.numm4)) / self.denn

        return self.a1_a, self.a2_a

    def draw(self, screen):
        self.x1 = int(self.x0 + self.r1 * np.sin(self.a1))
        self.y1 = int(self.y0 + self.r1 * np.cos(self.a1))
        self.x2 = int(self.x1 + self.r2 * np.sin(self.a2))
        self.y2 = int(self.y1 + self.r2 * np.cos(self.a2))

        pg.draw.circle(screen, (255, 255, 255), (self.x1, self.y1), 10)
        pg.draw.circle(screen, (255, 255, 255), (self.x2, self.y2), 10)
        pg.draw.line(screen, (255, 255, 255), (self.x0, self.y0), (self.x1, self.y1))
        pg.draw.line(screen, (255, 255, 255), (self.x1, self.y1), (self.x2, self.y2))

    def move(self):
        [self.a1_a, self.a2_a] = self.angles()
        # if abs(self.a1_v) > 3:
        #     print('ya')
        self.a1_v += self.a1_a * 0.5
        self.a2_v += self.a2_a * 0.5
        # else:
        # self.a1_v += self.a1_a #+ 0.0001
        # self.a2_v += self.a2_a# + 0.0001
        self.a1 += self.a1_v
        self.a2 += self.a2_v


class Sim:
    """Simulation object."""

    def __init__(self):
        pg.init()
        self.FPS = 30
        self.screen_width = 600
        self.screen_height = 600
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption("Double Pendulum")
        self.clock = pg.time.Clock()
        self.setup()

    def setup(self):
        self.double_pendulum = DoublePendulum(120, 120, 50, 50, np.pi / 2, np.pi / 2)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    self.setup()
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    def sim_loop(self):
        while 1:
            self.screen.fill((0, 0, 0))
            self.double_pendulum.draw(self.screen)
            self.double_pendulum.move()
            pg.display.update()
            self.clock.tick(self.FPS)
            self.events()


if __name__ == "__main__":
    Sim().sim_loop()
