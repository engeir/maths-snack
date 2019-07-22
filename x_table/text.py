import pygame as pg
import config as cf


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

    def text_objects(self, msg, font, color):
        text_surface = font.render(msg, True, color)
        return text_surface, text_surface.get_rect()

    def message_display(self, screen, msg, color, posx, posy, size):
        text = pg.font.Font('Ovo-Regular.ttf', size)
        TextSurf, TextRect = self.text_objects(msg, text, color)
        TextRect.topleft = (posx, posy)
        screen.blit(TextSurf, TextRect)

    def type(self, screen, factor, points):
        self.message_display(screen, f'Factor: {round(factor, 2)}', cf.WHITE, 20, 20, 40)
        self.message_display(screen, f'Points: {int(points)}', cf.WHITE, 20, 60, 40)
