import pygame as pg

import maths_snack.programs.wheelie.config as cf
from maths_snack.programs.utils.my_texts import Text
from maths_snack.programs.wheelie.circles import Circle, Wheel


class Sim:
    """Make the simulation of wheels on wheels."""

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(
            [cf.SCREEN_WIDTH, cf.SCREEN_HEIGHT], flags=pg.SCALED
        )
        # self.screen = pg.display.set_mode((0, 0), flags=pg.FULLSCREEN)
        pg.display.set_caption("Wheels on Wheels")
        self.clock = pg.time.Clock()
        self.write()
        self.choose_version = None
        self.mouse_pos()
        self.wait = True
        self.lines = 0
        self.setup()

    def setup(self):
        """When pressing 'r' this default setup is initiated."""
        self.choose_version = None
        self.wait = True
        self.lines = 0
        self.table = Circle()
        self.wheel = Wheel()
        self.factor = 0

    def events(self):
        """Take care of event handling."""
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    # pg.image.save(self.screen, 'x_table.png')
                    pg.quit()
                    quit()
                if event.key == pg.K_SPACE:
                    pass
                if event.key == pg.K_r:
                    self.setup()
                if event.key == pg.K_SPACE:
                    self.lines = (self.lines + 1) % 2
                    if self.lines:
                        self.factor -= 0.05
                if self.choose_version is not None and self.wait:
                    if event.key == pg.K_n:
                        self.wait = False
                        self.screen.fill(cf.PURPLE)
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if self.wait:
                press, _, _ = pg.mouse.get_pressed()
                if press:
                    self.wheel.draw_path(self.screen, self.x, self.y, pressed=True)
                if event.type == pg.MOUSEBUTTONUP:
                    for i, t in enumerate(self.text_choose_n):
                        if t.overlay(self.x, self.y):
                            self.choose_version = f"w{i}"
                            self.wheel.create_wheel(self.choose_version)
                            break

    def menu(self):
        self.mouse_pos()
        self.text_version.type(self.screen, cf.WHITE, size=cf.TXT_BIG)
        self.text_choose.type(self.screen, cf.WHITE, size=cf.TXT_BIG)
        self.text_draw_own.type(self.screen, cf.WHITE, size=cf.TXT_BIG)
        for t in self.text_choose_n:
            t.type(self.screen, cf.WHITE, size=cf.TXT_BIG)
        if self.choose_version is None:
            for t in self.text_choose_n:
                if t.overlay(self.x, self.y):
                    t.type(self.screen, cf.RED, fill=cf.PURPLE, size=cf.TXT_BIG)
                    break
        elif self.choose_version == "w0" and self.wait:
            self.screen.fill(cf.PURPLE)
            self.text_version.type(
                self.screen, cf.WHITE, text="Draw your own", size=cf.TXT_BIG
            )
            self.wheel.draw_path(self.screen, self.x, self.y)
            self.text_done_draw.type(self.screen, cf.WHITE, size=cf.TXT_SMALL)
        else:
            for i, t in enumerate(self.text_choose_n):
                if self.choose_version == f"w{i}":
                    t.type(self.screen, cf.GREEN, fill=cf.PURPLE, size=cf.TXT_BIG)
                    break
            self.text_press_n.type(self.screen, cf.WHITE, size=cf.TXT_BIG)

    def write(self):
        self.text_version = Text(
            "Choose your version",
            cf.SCREEN_WIDTH / 2,
            cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * 0.4,
        )
        self.text_draw_own = Text(
            "Draw your own",
            cf.SCREEN_WIDTH / 2,
            cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * 0.1,
        )
        self.text_choose = Text(
            "Version:",
            cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * 0.4,
            cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * 0.25,
            loc="l",
        )
        self.text_choose1 = Text(
            "1",
            cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * 0.2,
            cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * 0.25,
            loc="l",
        )
        self.text_choose2 = Text(
            "2",
            cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * 0.1,
            cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * 0.25,
            loc="l",
        )
        self.text_choose3 = Text(
            "3",
            cf.SCREEN_WIDTH / 2 - cf.SCREEN_WIDTH * 0.0,
            cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * 0.25,
            loc="l",
        )
        self.text_choose4 = Text(
            "4",
            cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * 0.1,
            cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * 0.25,
            loc="l",
        )
        self.text_choose5 = Text(
            "5",
            cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * 0.2,
            cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * 0.25,
            loc="l",
        )
        self.text_choose_n = [
            self.text_draw_own,
            self.text_choose1,
            self.text_choose2,
            self.text_choose3,
            self.text_choose4,
            self.text_choose5,
        ]
        self.text_press_n = Text(
            'Press "n".',
            cf.SCREEN_WIDTH / 2,
            cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * 0.2,
        )
        self.text_done_draw = Text(
            'Press "n" when\nyou are done',
            cf.SCREEN_WIDTH * 0.15,
            cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * 0.4,
            loc="l",
        )
        self.text_restart = Text(
            'Restart: "r"',
            cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * 0.48,
            cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * 0.47,
            loc="r",
        )
        self.text_quit = Text(
            'Quit: "esc"',
            cf.SCREEN_WIDTH / 2 + cf.SCREEN_WIDTH * 0.36,
            cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * 0.47,
            loc="r",
        )

    def mouse_pos(self):
        self.x, self.y = pg.mouse.get_pos()

    def circle_sim(self):
        if self.choose_version == "w0" and self.wheel.w is None:
            self.wheel.f_trans()
        self.table.draw(
            self.screen, self.wheel.w, self.factor, self.lines, self.choose_version
        )
        draw = ["start", "stop"]
        self.text_version.type(
            self.screen,
            cf.WHITE,
            size=cf.TXT_BIG,
            text=f"Press space to {draw[self.lines]} drawing",
        )
        self.text_restart.type(self.screen, cf.WHITE, size=cf.TXT_SMALL, fill=cf.PURPLE)
        self.text_quit.type(self.screen, cf.WHITE, size=cf.TXT_SMALL, fill=cf.PURPLE)
        if self.lines:
            self.factor += 0.05

    def game_loop(self):
        """The main loop that runs the simulation."""
        while 1:
            if self.wait:
                self.screen.fill(cf.PURPLE)
                self.menu()
            else:
                self.screen.fill(cf.PURPLE, self.text_version.get_rect())
                self.screen.fill(
                    cf.PURPLE, (0, 0, int(cf.SCREEN_WIDTH / 2), cf.SCREEN_HEIGHT)
                )
                self.circle_sim()
            pg.display.update()
            self.clock.tick(cf.FPS)
            self.events()


if __name__ == "__main__":
    Sim().game_loop()
