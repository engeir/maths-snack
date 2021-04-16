import random

import pygame as pg

# CONSTANTS
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 10000


class Barnsley:
    """Make an object that draws a fern."""

    def __init__(self):
        self.x = 0
        self.y = 0
        self.xprint = None
        self.yprint = None
        self.R = 0
        self.G = 0
        self.B = 0
        self.colX = 0
        self.colY = 0

    def make_point(self):
        r = random.randrange(0, 100, 1)
        if r < 1:
            self.x = 0
            self.y = 0.16 * self.y
        elif r < 86:
            self.x = 0.85 * self.x + 0.04 * self.y
            self.y = -0.04 * self.x + 0.85 * self.y + 1.6
        elif r < 93:
            self.x = 0.2 * self.x - 0.26 * self.y
            self.y = 0.23 * self.x + 0.22 * self.y + 1.6
        else:
            self.x = -0.15 * self.x + 0.28 * self.y
            self.y = 0.26 * self.x + 0.24 * self.y + 0.44

    def draw(self, screen):
        # −2.1820 < x < 2.6558
        # 0 ≤ y < 9.9983
        self.xprint = int(self.x * SCREEN_WIDTH * 0.1) + int(SCREEN_WIDTH * 0.45)
        self.yprint = -int(self.y * SCREEN_HEIGHT * 0.07) + int(SCREEN_HEIGHT * 0.85)
        self.colX = (self.x + 2.2) / 5.1
        self.colY = self.y / 12
        self.R = int((self.colY) * 255)
        self.G = int((self.colX) * 255)
        self.B = int((2 - self.colX - self.colY) * 255 / 2)
        screen.set_at((self.xprint, self.yprint), (self.R, self.G, self.B))


class Sim:
    """Simulate the making of the fern."""

    def __init__(self):
        pg.init()
        self.FPS = FPS
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption("Barnsley Fern")
        self.clock = pg.time.Clock()
        self.setup()
        self.a = 0

    def setup(self):
        self.fern = Barnsley()
        self.screen.fill((20, 2, 2))

    def events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    self.setup()
                if event.key == pg.K_ESCAPE:
                    # pg.image.save(self.screen, 'barnsley_fern.png')
                    pg.quit()
                    quit()
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    def sim_loop(self):
        while 1:
            self.fern.draw(self.screen)
            self.fern.make_point()
            # pg.display.flip()
            if self.a % 500 == 0:
                pg.display.update()
            # pg.transform.flip(self.screen, False, True)
            self.clock.tick(self.FPS)
            self.events()
            self.a += 1


if __name__ == "__main__":
    Sim().sim_loop()
