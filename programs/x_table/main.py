import sys
import pygame as pg
import config as cf
from x_table_calc import TimesTable
sys.path.append('../utils')
from texts import Text


class Sim:
    """Make the simulation of a times table."""

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0))
        pg.display.set_caption("Times Table")
        self.clock = pg.time.Clock()
        self.write()
        self.choose_version = None
        self.mouse_pos()
        self.wait = True
        self.ctrl_max_factor = None
        self.num = None
        self.setup()

    def setup(self):
        """When pressing 'r' this default setup is initiated.
        """
        self.table = TimesTable(20)
        self.text_version.type(self.screen, cf.WHITE)
        self.mouse_pos()
        self.menu()
        self.factor = 0
        self.adder = 0.01
        self.num = 20
        self.count = 0

    def events(self):
        """Take care of event handling.
        """
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    # pg.image.save(self.screen, 'x_table.png')
                    pg.quit()
                    quit()
                if event.key == pg.K_SPACE:
                    pass
                if event.key == pg.K_r:
                    self.choose_version = None
                    self.wait = True
                    self.ctrl_max_factor = None
                    self.num = None
                if self.choose_version is not None and self.wait:
                    if event.key == pg.K_n:
                        self.wait = False
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if self.wait:
                if event.type == pg.MOUSEBUTTONUP:
                    if self.text_auto.overlay(self.x, self.y):
                        self.choose_version = 'auto'
                    elif self.text_ctrl.overlay(self.x, self.y):
                        self.choose_version = 'ctrl'
                    elif self.text_max_auto.overlay(self.x, self.y):
                        self.choose_version = 'max_auto'

    def menu(self):
        if self.choose_version is None:
            if self.text_auto.overlay(self.x, self.y):
                self.text_auto.type(self.screen, cf.RED)
            else:
                self.text_auto.type(self.screen, cf.WHITE)
            if self.text_ctrl.overlay(self.x, self.y):
                self.text_ctrl.type(self.screen, cf.RED)
            else:
                self.text_ctrl.type(self.screen, cf.WHITE)
            if self.text_max_auto.overlay(self.x, self.y):
                self.text_max_auto.type(self.screen, cf.RED)
            else:
                self.text_max_auto.type(self.screen, cf.WHITE)
        elif self.choose_version == 'auto':
            self.factor = 0
            self.text_auto.type(self.screen, cf.GREEN)
            self.text_ctrl.type(self.screen, cf.WHITE)
            self.text_max_auto.type(self.screen, cf.WHITE)
        elif self.choose_version == 'ctrl':
            self.text_auto.type(self.screen, cf.WHITE)
            self.text_ctrl.type(self.screen, cf.GREEN)
            self.text_max_auto.type(self.screen, cf.WHITE)
        elif self.choose_version == 'max_auto':
            self.factor = 0
            self.text_auto.type(self.screen, cf.WHITE)
            self.text_ctrl.type(self.screen, cf.WHITE)
            self.text_max_auto.type(self.screen, cf.GREEN)
        if self.choose_version is not None and self.wait:
            self.text_press_n.type(self.screen, cf.WHITE)

    def write(self):
        self.text_version = Text(f'What version do you want?', cf.SCREEN_WIDTH / 2,
                                 cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .4)
        self.text_auto = Text(f'Auto (increasing number of points)', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .4,
                              cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .25, loc='l')
        self.text_max_auto = Text(f'Auto (constant number of points)', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .4,
                                  cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .15, loc='l')
        self.text_ctrl = Text(f'Full control', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .4,
                              cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .05, loc='l')
        self.text_max_factor = Text(f'Set the max factor value.', cf.SCREEN_WIDTH / 2,
                                    cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .1)
        self.text_press_n = Text(f'Press "n".', cf.SCREEN_WIDTH / 2,
                                 cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * .2)
        self.text_factor = Text('', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .45,
                                cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .4, loc='l')
        self.text_points = Text('', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .45,
                                cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .32, loc='l')

    def mouse_pos(self):
        self.x, self.y = pg.mouse.get_pos()

    def full_control(self):
        w = self.x * 201 / cf.SCREEN_WIDTH
        h = cf.SCREEN_HEIGHT - self.y
        h *= 90 / cf.SCREEN_HEIGHT
        self.table.draw(self.screen, h, int(w))
        self.text_factor.type(
            self.screen, cf.WHITE, text=f'Factor: {round(h, 2)}')
        self.text_points.type(
            self.screen, cf.WHITE, text=f'Points: {int(w)}')

    def full_auto(self):
        if self.num <= 200:
            self.table.draw(self.screen, self.factor, self.num)
        if self.count % 2 == 0 and self.num < 200:
            self.num += 1
        self.text_factor.type(
            self.screen, cf.WHITE, text=f'Factor: {round(self.factor, 2)}')
        self.text_points.type(
            self.screen, cf.WHITE, text=f'Points: {int(self.num)}')
        self.factor += self.adder
        self.adder += 0.001
        self.count += 1

    def auto_max(self):
        self.num = 200
        self.table.draw(self.screen, self.factor, self.num)
        self.text_factor.type(self.screen, cf.WHITE,
                              text=f'Factor: {round(self.factor, 2)}')
        self.text_points.type(self.screen, cf.WHITE,
                              text=f'Points: {int(self.num)}')
        self.factor += self.adder
        self.adder += 0.0001

    def game_loop(self):
        """The main loop that runs the simulation."""
        while 1:
            self.screen.fill(cf.PURPLE)
            if self.wait:
                self.setup()
            else:
                if self.choose_version == 'ctrl':
                    self.mouse_pos()
                    self.full_control()
                elif self.choose_version == 'auto':
                    self.full_auto()
                elif self.choose_version == 'max_auto':
                    self.auto_max()
            pg.display.update()
            self.clock.tick(cf.FPS)
            self.events()


if __name__ == "__main__":
    Sim().game_loop()
