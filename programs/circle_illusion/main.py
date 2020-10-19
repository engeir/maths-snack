import sys
import pygame as pg
import config as cf
from circle import Circle
sys.path.append('../utils')
from my_texts import Text


class Sim:
    """Make the simulation of a rolling circle."""

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0))
        pg.display.set_caption("Circle Illusion")
        self.clock = pg.time.Clock()
        self.write()
        self.choose_version = None
        self.mouse_pos()
        self.wait = True
        self.ctrl_max_factor = None
        self.lines = 0
        self.circle = 0
        self.num = None
        self.factor = 0
        self.setup()

    def setup(self):
        """When pressing 'r' this default setup is initiated.
        """
        self.table = Circle(20)
        self.text_version.type(self.screen, cf.WHITE)
        self.mouse_pos()
        self.menu()

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
                    self.lines = 0
                if event.key == pg.K_l:
                    self.lines = (self.lines + 1) % 2
                if event.key == pg.K_c:
                    self.circle = (self.circle + 1) % 2
                if self.choose_version is not None and self.wait:
                    if event.key == pg.K_n:
                        self.wait = False
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if self.wait:
                if event.type == pg.MOUSEBUTTONUP:
                    self.num = int((self.x / cf.SCREEN_WIDTH) * 100)
                    self.choose_version = 'circ'

    def menu(self):
        if self.choose_version is None:
            self.text_choose.type(self.screen, cf.WHITE,
                                  text=f'Points: {int((self.x / cf.SCREEN_WIDTH) * 100)}')
        elif self.choose_version == 'circ':
            self.text_choose.type(self.screen, cf.GREEN,
                                  text=f'Points: {self.num}')
        if self.choose_version is not None and self.wait:
            self.text_press_n.type(self.screen, cf.WHITE)

    def write(self):
        self.text_version = Text(f'How many points do you want?', cf.SCREEN_WIDTH / 2,
                                 cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .4)
        self.text_choose = Text(f'', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .4,
                                cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .25, loc='l')
        self.text_press_n = Text(f'Press "n".', cf.SCREEN_WIDTH / 2,
                                 cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * .2)
        self.text_points = Text('', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .45,
                                cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .24, loc='l')
        self.text_lines = Text('', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .45,
                               cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .4, loc='l')
        self.text_circ = Text('', cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * .45,
                              cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .32, loc='l')
        self.text_restart = Text('Restart: "R"', cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * .45,
                                 cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .32, loc='r')
        self.text_quit = Text('Quit: "esc"', cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * .45,
                              cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * .4, loc='r')

    def mouse_pos(self):
        self.x, self.y = pg.mouse.get_pos()

    def circle_sim(self):
        self.table.draw(self.screen, self.factor, self.num, self.lines, self.circle)
        self.text_points.type(self.screen, cf.WHITE,
                              text=f'Points: {int(self.num)}')
        line_str = ['Show', 'Hide']
        self.text_lines.type(self.screen, cf.WHITE, text=f'{line_str[self.lines]} lines: "L"')
        self.text_circ.type(self.screen, cf.WHITE, text=f'{line_str[self.circle]} circle: "C"')
        self.text_restart.type(self.screen, cf.WHITE, size=30)
        self.text_quit.type(self.screen, cf.WHITE, size=30)
        self.factor = self.factor % 360
        self.factor += 0.05

    def game_loop(self):
        """The main loop that runs the simulation."""
        while 1:
            self.screen.fill(cf.PURPLE)
            if self.wait:
                self.setup()
            else:
                self.circle_sim()
            pg.display.update()
            self.clock.tick(cf.FPS)
            self.events()


if __name__ == "__main__":
    Sim().game_loop()
