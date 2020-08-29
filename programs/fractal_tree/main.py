import time
import pygame as pg
import config as cf
from tree import Tree


class Sim:
    """Make the simulation of a times table."""

    def __init__(self):
        pg.init()
        # a = pg.display.list_modes()
        # self.screen = pg.display.set_mode(a[0], pg.FULLSCREEN)
        self.screen = pg.display.set_mode((0, 0))
        pg.display.set_caption("Fractal Tree")
        self.clock = pg.time.Clock()
        self.grow = 0
        self.new = True
        self.start = False
        self.setup()

    def setup(self):
        """When pressing 'r' this default setup is initiated.
        """
        self.grow = cf.GROW_SPEED
        self.tree = Tree()
        self.generation = 0
        self.screen.fill(cf.PURPLE)
        self.tree.draw(self.screen, self.generation, self.grow)

    def events(self):
        """Take care of event handling.
        """
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    # pg.image.save(self.screen, 'fractal_tree.png')
                    pg.quit()
                    quit()
                if event.key == pg.K_SPACE:
                    pass
                if event.key == pg.K_r:
                    self.new = True
                    self.setup()
                # if event.key == pg.K_n:
                #     self.grow = 0.1
                #     self.tree.structure(self.generation)
                #     self.generation += 1
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    def growing(self):
        if self.grow + cf.GROW_SPEED < 1.06:
            self.grow += cf.GROW_SPEED
        if self.grow > 1.04 and self.generation < 8:
            self.grow = cf.GROW_SPEED
            self.tree.structure(self.generation)
            self.generation += 1

    def slow_start(self):
        if self.start:
            time.sleep(1)
            self.start = False
        if self.new:
            self.new = False
            self.start = True

    def game_loop(self):
        """The main loop that runs the simulation."""
        while 1:
            self.growing()
            self.tree.draw(self.screen, self.generation, self.grow)
            pg.display.update()
            self.clock.tick(cf.FPS)
            self.events()
            self.slow_start()


if __name__ == "__main__":
    Sim().game_loop()
