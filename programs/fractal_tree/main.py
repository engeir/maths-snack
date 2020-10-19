import sys
import time
import pygame as pg
import config as cf
from tree import Tree
sys.path.append('../utils')
from my_texts import Text


class Sim:
    """Make the simulation of a times table."""

    def __init__(self):
        pg.init()
        # a = pg.display.list_modes()
        # self.screen = pg.display.set_mode(a[0], pg.FULLSCREEN)
        self.screen = pg.display.set_mode((0, 0))
        pg.display.set_caption("Fractal Tree")
        self.clock = pg.time.Clock()
        self.reproduction = [False, None]
        self.angle = [False, None]
        self.scale = [False, None]
        self.write()
        self.mouse_pos()
        self.wait = True
        self.grow = 0
        self.new = True
        self.start = False
        self.setup()

    def setup(self):
        """When pressing 'r' this default setup is initiated.
        """
        self.reproduction = [False, None]
        self.angle = [False, None]
        self.scale = [False, None]
        self.wait = True
        self.grow = cf.GROW_SPEED
        self.tree = Tree()
        self.generation = 0
        self.screen.fill(cf.PURPLE)

    def menu(self):
        self.mouse_pos()
        self.text_version.type(self.screen, cf.WHITE, size=cf.TXT_BIG)
        self.text_choose_a.type(self.screen, cf.WHITE, text=f'{self.angle[1]}', size=cf.TXT_BIG)
        self.text_choose_r.type(self.screen, cf.WHITE, text=f'{self.reproduction[1]}', size=cf.TXT_BIG)
        self.text_choose_s.type(self.screen, cf.WHITE, text=f'0.{self.scale[1]}', size=cf.TXT_BIG)
        for t in self.text_choose_n:
            t.type(self.screen, cf.WHITE, size=cf.TXT_BIG)
        for i, t in enumerate(self.text_choose_n):
            if t.overlay(self.x, self.y):
                if i == 1:
                    if self.reproduction[0]:
                        t.type(self.screen, cf.GREEN, fill=cf.PURPLE, size=cf.TXT_BIG)
                    else:
                        t.type(self.screen, cf.RED, fill=cf.PURPLE, size=cf.TXT_BIG)
                elif i == 0:
                    if self.angle[0]:
                        t.type(self.screen, cf.GREEN, fill=cf.PURPLE, size=cf.TXT_BIG)
                    else:
                        t.type(self.screen, cf.RED, fill=cf.PURPLE, size=cf.TXT_BIG)
                elif i == 2:
                    if self.scale[0]:
                        t.type(self.screen, cf.GREEN, fill=cf.PURPLE, size=cf.TXT_BIG)
                    else:
                        t.type(self.screen, cf.RED, fill=cf.PURPLE, size=cf.TXT_BIG)
                break
        if self.reproduction[1] is not None and self.angle[1] is not None and self.scale[1] is not None and self.wait:
            self.text_version.type(self.screen, cf.WHITE, size=cf.TXT_BIG)
            # self.text_done_draw.type(self.screen, cf.WHITE, size=cf.TXT_SMALL)
            for t in self.text_choose_n:
                t.type(self.screen, cf.WHITE, size=cf.TXT_BIG)
            self.text_press_n.type(self.screen, cf.WHITE, size=cf.TXT_BIG)

    def write(self):
        self.text_version = Text(f'Choose your version', cf.SCREEN_WIDTH / 2,
                                 cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .4)
        self.text_angle = Text(f'Angle spacing:', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .4,
                               cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .1, loc='l')
        self.text_repr = Text(f'Reproduction number:', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .4,
                              cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .25, loc='l')
        self.text_scale = Text(f'Scaling:', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .4,
                              cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * .05, loc='l')
        self.text_choose_a = Text(f'{self.angle[1]}', cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * .1,
                                  cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .1, loc='l')
        self.text_choose_r = Text(f'{self.reproduction[1]}', cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * .1,
                                  cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .25, loc='l')
        self.text_choose_s = Text(f'{self.scale[1]}', cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * .1,
                                  cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * .05, loc='l')
        self.text_choose_n = [self.text_angle,
                              self.text_repr,
                              self.text_scale]
        self.text_press_n = Text(f'Press "n".', cf.SCREEN_WIDTH / 2,
                                 cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * .2)
        # self.text_done_draw = Text('Press "n" when\nyou are done', cf.SCREEN_WIDTH * .05,
        #                            cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .4, loc='l')
        self.text_restart = Text('Restart: "r"', cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * .48,
                                 cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .47, loc='r')
        self.text_quit = Text('Quit: "esc"', cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * .36,
                              cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .47, loc='r')

    def mouse_pos(self):
        self.x, self.y = pg.mouse.get_pos()

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
                if event.key == pg.K_n:
                    self.screen.fill(cf.PURPLE)
                    self.wait = False
                    self.tree.set_vars(self.reproduction[1], self.angle[1], self.scale[1])
                    self.tree.draw(self.screen, self.generation, self.grow)
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if self.wait:
                if event.type == pg.MOUSEBUTTONUP:
                    for i, t in enumerate(self.text_choose_n):
                        if t.overlay(self.x, self.y):
                            if i == 1:
                                self.reproduction[0] = True
                                self.angle[0] = False
                                self.scale[0] = False
                            elif i == 0:
                                self.angle[0] = True
                                self.reproduction[0] = False
                                self.scale[0] = False
                            elif i == 2:
                                self.angle[0] = False
                                self.reproduction[0] = False
                                self.scale[0] = True
                            break
                if self.reproduction[0]:
                    self.set_dial(event, self.reproduction)
                if self.angle[0]:
                    self.set_dial(event, self.angle)
                if self.scale[0]:
                    self.set_dial(event, self.scale)

    def set_dial(self, e, kind):
        key_map = {'48': 0, '49': 1, '50': 2, '51': 3, '52': 4, '53': 5, '54': 6, '55': 7, '56': 8, '57': 9}
        if e.type == pg.KEYDOWN:
            if e.key in [pg.K_0, pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9]:
                val = key_map[str(e.key)]
                if kind[1] is None:
                    kind[1] = val
                else:
                    kind[1] = int(10 * kind[1] + val)

    def growing(self):
        if self.grow + cf.GROW_SPEED < 1.06:
            self.grow += cf.GROW_SPEED
        if self.grow > 1.04 and self.generation < cf.GENS:
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
            if self.wait:
                self.screen.fill(cf.PURPLE)
                self.menu()
            else:
                self.growing()
                self.tree.draw(self.screen, self.generation, self.grow)
                self.text_restart.type(self.screen, cf.WHITE, size=cf.TXT_SMALL)
                self.text_quit.type(self.screen, cf.WHITE, size=cf.TXT_SMALL)
            pg.display.update()
            self.clock.tick(cf.FPS)
            self.events()
            self.slow_start()


if __name__ == "__main__":
    Sim().game_loop()
