import sys
import pygame as pg
import numpy as np
import config as cf
from dragon import Dragon
sys.path.append('../utils')
from texts import Text


class Sim:
    """Make a simulation of a beautiful Dragon curve."""

    def __init__(self):
        pg.init()
        # a = pg.display.list_modes()
        # self.screen = pg.display.set_mode(a[0], pg.FULLSCREEN)
        self.screen = pg.display.set_mode((0, 0))
        pg.display.set_caption("Dragon Curve")
        self.clock = pg.time.Clock()
        self.write()
        self.wait = True
        self.angle = 0
        self.dragon_tails = 0
        self.x = self.y = 0
        self.auto = None
        self.dragon_size = None
        self.first_line = False
        self.setup()

    def setup(self):
        """When pressing 'r' this default setup is initiated.
        """
        self.angle = 0
        self.dragon_tails = 1
        self.screen.fill(cf.PURPLE)
        self.text_a_or_m.type(self.screen, cf.WHITE)
        self.text_esc_r.type(self.screen, cf.WHITE)
        if self.auto is None:
            if self.text_auto.overlay(self.x, self.y):
                self.text_auto.type(self.screen, cf.RED)
            else:
                self.text_auto.type(self.screen, cf.WHITE)
            if self.text_manual.overlay(self.x, self.y):
                self.text_manual.type(self.screen, cf.RED)
            else:
                self.text_manual.type(self.screen, cf.WHITE)
        elif self.auto:
            self.text_auto.type(self.screen, cf.GREEN)
            self.text_manual.type(self.screen, cf.WHITE)
        else:
            self.text_auto.type(self.screen, cf.WHITE)
            self.text_manual.type(self.screen, cf.GREEN)
        if self.auto is not None:
            self.text_dragon_size.type(self.screen, cf.WHITE)
        if self.auto is not None and self.dragon_size is None:
            if self.text_2.overlay(self.x, self.y):
                self.text_2.type(self.screen, cf.RED)
            else:
                self.text_2.type(self.screen, cf.WHITE)
            if self.text_3.overlay(self.x, self.y):
                self.text_3.type(self.screen, cf.RED)
            else:
                self.text_3.type(self.screen, cf.WHITE)
            if self.text_5.overlay(self.x, self.y):
                self.text_5.type(self.screen, cf.RED)
            else:
                self.text_5.type(self.screen, cf.WHITE)
            if self.text_40.overlay(self.x, self.y):
                self.text_40.type(self.screen, cf.RED)
            else:
                self.text_40.type(self.screen, cf.WHITE)
        if self.dragon_size == 1:
            self.text_2.type(self.screen, cf.GREEN)
            self.text_3.type(self.screen, cf.WHITE)
            self.text_5.type(self.screen, cf.WHITE)
            self.text_40.type(self.screen, cf.WHITE)
        elif self.dragon_size == 2:
            self.text_2.type(self.screen, cf.WHITE)
            self.text_3.type(self.screen, cf.GREEN)
            self.text_5.type(self.screen, cf.WHITE)
            self.text_40.type(self.screen, cf.WHITE)
        elif self.dragon_size == 3:
            self.text_2.type(self.screen, cf.WHITE)
            self.text_3.type(self.screen, cf.WHITE)
            self.text_5.type(self.screen, cf.GREEN)
            self.text_40.type(self.screen, cf.WHITE)
        elif self.dragon_size == 4:
            self.text_2.type(self.screen, cf.WHITE)
            self.text_3.type(self.screen, cf.WHITE)
            self.text_5.type(self.screen, cf.WHITE)
            self.text_40.type(self.screen, cf.GREEN)
        if self.auto is not None and self.dragon_size is not None:
            self.dragon = Dragon(self.auto, self.dragon_size)
            self.screen.fill(cf.PURPLE)
            if self.auto:
                self.text_press_n.type(self.screen, cf.WHITE)
            else:
                self.text_press_n_a_lot.type(self.screen, cf.WHITE)

    def events(self):
        """Take care of event handling.
        """
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    # pg.image.save(self.screen, 'dragon_curve.png')
                    pg.quit()
                    quit()
                if event.key == pg.K_SPACE:
                    pass
                if event.key == pg.K_r:
                    self.wait = True
                    self.auto = None
                    self.dragon_size = None
                    self.first_line = False
                    self.setup()
                if self.auto is not None and self.dragon_size is not None:
                    if event.key == pg.K_n:
                        self.wait = False
                        if not self.auto:
                            if self.first_line:
                                self.dragon.structure()
                            else:
                                self.first_line = True
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if self.wait:
                if event.type == pg.MOUSEBUTTONUP:
                    if self.text_auto.l < self.x and self.x < self.text_auto.r and \
                            self.text_auto.t < self.y and self.y < self.text_auto.b:
                        self.auto = True
                    elif self.text_manual.l < self.x and self.x < self.text_manual.r and \
                            self.text_manual.t < self.y and self.y < self.text_manual.b:
                        self.auto = False
                    if self.auto is not None:
                        if self.text_2.l < self.x and self.x < self.text_2.r and \
                                self.text_2.t < self.y and self.y < self.text_2.b:
                            self.dragon_size = 1
                        if self.text_3.l < self.x and self.x < self.text_3.r and \
                                self.text_3.t < self.y and self.y < self.text_3.b:
                            self.dragon_size = 2
                        if self.text_5.l < self.x and self.x < self.text_5.r and \
                                self.text_5.t < self.y and self.y < self.text_5.b:
                            self.dragon_size = 3
                        if self.text_40.l < self.x and self.x < self.text_40.r and \
                                self.text_40.t < self.y and self.y < self.text_40.b:
                            self.dragon_size = 4

    def write(self):
        self.text_esc_r = Text('If in doubt, press "r". Press "esc" to quit.', cf.SCREEN_WIDTH / 2,
                               cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * .3)
        self.text_press_n = Text('Press "n".', cf.SCREEN_WIDTH / 2, cf.SCREEN_HEIGHT / 2)
        self.text_press_n_a_lot = Text('Press "n". Repeatedly.', cf.SCREEN_WIDTH / 2, cf.SCREEN_HEIGHT / 2)
        self.text_a_or_m = Text('Automatic or Manual Simulation?', cf.SCREEN_WIDTH / 2,
                                cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .35)
        self.text_auto = Text('Automatic', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .2,
                              cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .2)
        self.text_manual = Text('Manual', cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * .2,
                                cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .2)
        self.text_dragon_size = Text('Choose the length of the lines in your Dragon.', cf.SCREEN_WIDTH / 2,
                                     cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .05)
        self.text_2 = Text('2', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .2,
                           cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * .1)
        self.text_3 = Text('3', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .07,
                           cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * .1)
        self.text_5 = Text('5', cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * .07,
                           cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * .1)
        self.text_40 = Text('40', cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * .2,
                            cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * .1)

    def mouse_pos(self):
        self.x, self.y = pg.mouse.get_pos()

    def game_loop(self):
        """The main loop that runs the simulation."""
        while 1:
            if not self.wait:
                if self.angle < np.pi / 2:
                    self.angle += 0.1
                else:
                    self.dragon_tails += 1
                    self.angle = 0
                self.screen.fill(cf.PURPLE)
                self.dragon.draw(self.screen, self.angle, self.dragon_tails)
            else:
                self.mouse_pos()
                self.setup()
            pg.display.update()
            self.clock.tick(cf.FPS)
            self.events()


if __name__ == "__main__":
    Sim().game_loop()
