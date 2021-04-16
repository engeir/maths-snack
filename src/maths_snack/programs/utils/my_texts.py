import pygame as pg


class Text:
    """Class that show text to the screen.

    Copied from https: // pythonprogramming.net/displaying-text-pygame-screen/.

    Changed to better fit the rest of the code.
    Decide font type og text size before the surrounding box is obtained.
    The box's center is decided by 'posx' and 'posy', and the text-object is blitted to the screen.

    : param msg: the text you wish on screen
    : param color: the color of the text
    : param posx: x-pos of the text
    : param posy: y-pos of the text
    : param size: text size
    """

    def __init__(self, text, pos_x, pos_y, loc=False):
        self.text = text
        self.loc = loc
        self.pos_x, self.pos_y = pos_x, pos_y
        self.ell = 0
        self.r = 0
        self.t = 0
        self.b = 0

    @staticmethod
    def text_objects(msg, font, color):
        text_surface = font.render(msg, True, color)
        return text_surface, text_surface.get_rect()

    def message_display(self, screen, msg, color, posx, posy, size):
        # self.move(msg, color, posx, posy, size)
        text = pg.font.Font("src/maths_snack/programs/utils/Ovo-Regular.ttf", size)
        TextSurf, TextRect = self.text_objects(msg, text, color)
        if self.loc in ["left"]:
            TextRect.midleft = (posx, posy)
        elif self.loc in ["r", "right"]:
            TextRect.midright = (posx, posy)
        else:
            TextRect.center = (posx, posy)
        self.ell, self.r = TextRect.left, TextRect.right
        self.t, self.b = TextRect.top, TextRect.bottom
        screen.blit(TextSurf, TextRect)

    def type(self, screen, color, text=None, size=50, fill=False):
        if fill:
            screen.fill(fill, self.get_rect())
        if text is None:
            self.message_display(screen, self.text, color, self.pos_x, self.pos_y, size)
        else:
            self.message_display(screen, text, color, self.pos_x, self.pos_y, size)

    def overlay(self, x, y):
        return bool(self.ell < x < self.r and self.t < y < self.b)

    def get_rect(self):
        return (self.ell, self.t, self.r - self.ell, self.b - self.t)
