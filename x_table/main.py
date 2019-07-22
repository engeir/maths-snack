import numpy as np
import pygame as pg
import config as cf
from x_table import TimesTable
from text import Text


class Sim:
    """Make the simulation of a times table."""

    def __init__(self):
        self.setup()
        pg.init()
        self.screen = pg.display.set_mode((cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT))
        pg.display.set_caption("Times Table")
        self.clock = pg.time.Clock()

    def setup(self):
        """When pressing 'r' this default setup is initiated.
        """
        self.factor = 0
        self.num = 20
        self.table = TimesTable(self.num)
        self.count = 0
        self.text = Text()
        while 1:
            try:
                self.version = str(input('Type "ctrl" for full control over the animation, or "auto" to make it run on its own. '))
                if self.version != 'ctrl' and self.version != 'auto':
                    raise Exception
            except Exception:
                print('You need to type in either "ctrl" or "auto".')
            else:
                break

    def events(self):
        """Take care of event handling.
        """
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()
                if event.key == pg.K_SPACE:
                    pass
                if event.key == pg.K_r:
                    self.setup()
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    def full_control(self):
        w, h = pg.mouse.get_pos()
        w *= 200 / cf.SCREEN_WIDTH
        h *= - 30 / cf.SCREEN_WIDTH
        self.table.draw(self.screen, h, int(w))
        self.text.type(self.screen, h, w)

    def full_auto(self):
        if self.num <= 200:
            self.table.draw(self.screen, - self.factor, self.num)
        if self.count % 2 == 0 and self.num < 200:
            self.num += 1
        self.factor += 0.01
        self.count += 1
        self.text.type(self.screen, self.factor, self.num)

    def game_loop(self):
        """The main loop that runs the simulation."""
        while 1:
            self.screen.fill(cf.PURPLE)
            if self.version == 'ctrl':
                self.full_control()
            elif self.version == 'auto':
                self.full_auto()
            pg.display.update()
            self.clock.tick(cf.FPS)
            self.events()


if __name__ == "__main__":
    Sim().game_loop()
