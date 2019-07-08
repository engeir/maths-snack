import numpy as np
import pygame as pg


# CONSTANTS
SCREEN_WIDTH = 900
SCREEN_HEIGHT = SCREEN_WIDTH
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class TheGame:
    """Make the simulation/game."""

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Name")
        self.clock = pg.time.Clock()
        self.setup()

    def setup(self):
        """When pressing 'r' this default setup is initiated.
        """
        pass

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
            if event.type == pg.MOUSEBUTTONUP and self.choose == 0:
                pass

    def game_loop(self):
        """The main loop that runs the simulation."""
        while 1:
            self.screen.fill(WHITE)
            pg.display.update()
            self.clock.tick(FPS)
            self.events()


if __name__ == "__main__":
    TheGame().game_loop()
