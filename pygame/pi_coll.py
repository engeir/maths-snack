import time
import numpy as np
import pygame as pg
from blocks import Block


# CONSTANTS
SCREEN_WIDTH = 900
SCREEN_HEIGHT = SCREEN_WIDTH
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (20, 20, 150)
TEXT_SIZE = 14
TEXT_POS = [200, 800]
TEXTBOX_SIZE = [50, 400]
TIME_STEP = 10000


class TheGame:
    """Make the simulation/game."""

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Name")
        self.clock = pg.time.Clock()
        self.count = 0
        self.click = pg.mixer.Sound('Click2-Sebastian-759472264.wav')
        self.setup()

    def setup(self):
        """When pressing 'r' this default setup is initiated.
        """
        self.small = Block(350, 1, 60, 0)
        self.big = Block(800, 100**5, 150, 10 / TIME_STEP)

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
            if event.type == pg.MOUSEBUTTONUP:
                pass

    def text_objects(self, msg, font, color):
        u"""Kopiert fra https://pythonprogramming.net/displaying-text-pygame-screen/.

        Endret for å passe bedre til koden ellers.

        :param msg: Teksten man ønsker å vise på skjermen.
        :param font: Fonttype og tekststørrelse.

        Bestem størrelsen til boksen som trengs for å vise teksten ved å returnere et rektangel som omkranser teksten.
        Returnerer teksten som 'text_surface' og den omkransende boksen.
        """
        text_surface = font.render(msg, True, color)
        return text_surface, text_surface.get_rect()

    def message_display(self, msg, color, posx, posy, size, screen):
        u"""Kopiert fra https://pythonprogramming.net/displaying-text-pygame-screen/.

        Endret for å passe bedre til koden ellers.

        :param msg: Teksten man ønsker å vise på skjermen.
        :param color: Fargen til teksten.
        :param posx: Horisontal posisjon til teksten.
        :param posy: Vertikal posisjon til teksten.
        :param size: Tekststørrelse.

        Bestem først fonttype og tekststørrelse før man får teksen og den omkransende boksen fra 'text_objects'-metoden.
        Boksens senter bestemmes av 'posx' og 'posy', og tekst-objektet blir blittet til skjermen.
        """
        text = pg.font.Font('freesansbold.ttf', size)
        TextSurf, TextRect = self.text_objects(msg, text, color)
        TextRect.center = (posx, posy)
        screen.blit(TextSurf, TextRect)

    def cons_of_energy(self, u1, m1, u2, m2):
        v1 = (m1 - m2) * u1 / (m1 + m2) + 2 * m2 * u2 / (m1 + m2)
        v2 = 2 * m1 * u1 / (m1 + m2) + (m2 - m1) * u2 / (m1 + m2)
        return v1, v2

    def collide(self):
        if self.small.x <= 150:
            pg.mixer.Sound.play(self.click)
            self.small.v = abs(self.small.v)
            self.count += 1
        if self.big.x <= (self.small.x + self.small.w):
            pg.mixer.Sound.play(self.click)
            self.small.v, self.big.v = self.cons_of_energy(
                self.small.v, self.small.m, self.big.v, self.big.m)
            self.count += 1

    def draw_all(self, screen):
        self.small.draw(screen, 'small')
        self.big.draw(screen, 'big')

    def move_all(self):
        self.small.move()
        self.big.move()

    def game_loop(self):
        """The main loop that runs the simulation."""
        while 1:
            box = self.screen.get_rect().clip((150, 0, 750, 700))
            pg.draw.lines(self.screen, WHITE, False,
                          [(150, 0), (150, 700), (900, 700)], 3)
            self.screen.fill(BLUE, box)
            for i in range(TIME_STEP):
                self.move_all()
                self.collide()
            self.draw_all(self.screen)
            self.message_display("# " + str(self.count), WHITE,
                                 (600), (200), 70, self.screen)
            pg.display.update()
            self.clock.tick(FPS)
            self.events()
            # if self.small.v < self.big.v and self.small.v > 0:
            #     time.sleep(3)
            #     quit()


if __name__ == "__main__":
    TheGame().game_loop()
