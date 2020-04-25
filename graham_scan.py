from math import atan2
from random import randint
import pygame as pg

FPS = 30
SCREEN_WIDTH = SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
GREEN = (20, 255, 150)
PURPLE = (20, 2, 2)


class Sim:
    """Make the simulation of a times table."""

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Graham Scan")
        self.clock = pg.time.Clock()
        self.setup()

    def setup(self):
        self.screen.fill(PURPLE)
        self.main()
        pg.display.update()

    def events(self):
        """Take care of event handling.
        """
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    # pg.image.save(self.screen, 'graham_scan.png')
                    pg.quit()
                    quit()
                if event.key == pg.K_SPACE:
                    pass
                if event.key == pg.K_r:
                    self.setup()
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    # Is the turn counter clockwise?
    @staticmethod
    def counter_clockwise(p1, p2, p3):
        return (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0])

    # Find the polar angle of a point relative to a reference point
    @staticmethod
    def polar_angle(ref, point):
        return atan2(point[1] - ref[1], point[0] - ref[0])

    def graham_scan(self, gift):
        gift = list(set(gift))  # Remove duplicate points
        start = min(gift, key=lambda p: (p[1], p[0]))  # Must be in hull
        gift.remove(start)

        s = sorted(gift, key=lambda point: self.polar_angle(start, point))
        hull = [start, s[0], s[1]]

        # Remove points from hull that make the hull concave
        for pt in s[2:]:
            while not self.counter_clockwise(hull[-2], hull[-1], pt):
                del hull[-1]
            hull.append(pt)

        return hull

    def main(self):
        # test_gift = [(-5, 2), (5, 7), (-6, -12), (-14, -14), (9, 9),
        #              (-1, -1), (-10, 11), (-6, 15), (-6, -8), (15, -9),
        #              (7, -7), (-2, -9), (6, -5), (0, 14), (2, 8)]
        test_gift = [(randint(50, SCREEN_WIDTH - 50),
                      randint(50, SCREEN_HEIGHT - 50)) for _ in range(500)]
        hull = self.graham_scan(test_gift)

        for x, y in test_gift:
            pg.draw.circle(self.screen, WHITE, (x, y), 4, 0)

        pg.draw.polygon(self.screen, GREEN, hull, 1)

        print("The points in the hull are:")
        for point in hull:
            print(point)

    def game_loop(self):
        """The main loop that runs the simulation."""
        while 1:
            self.clock.tick(FPS)
            self.events()

if __name__ == "__main__":
    Sim().game_loop()
