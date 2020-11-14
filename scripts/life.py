import numpy as np
import pygame as pg


# CONSTANTS
SCREEN_WIDTH = 900
SCREEN_HEIGHT = SCREEN_WIDTH
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
UNIVERSE_SIZE = 150  # 150
SCALING = int(SCREEN_WIDTH / UNIVERSE_SIZE)


class TheGame:
    """Make the universe for Conway's game of life."""

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Conway's Game of Life")
        self.clock = pg.time.Clock()
        self.seeds = {
            1: "Diehard",
            2: "Block Switch Engine",
            3: "Pentadecathlon",
            4: "Spaceship",
            5: "Boat",
            6: "P-pentomino",
            7: "Beacon",
            8: "Acorn",
            9: "Infinite",
            10: "Glider gun"
        }
        self.setup()

    def setup(self):
        while True:
            try:
                self.choose = int(
                    input('Custom or default?\nC = 0\nD = \t1 - Diehard\n\t2 - Block Switch Engine\n\t3 - Pentadecathlon\n\t4 - Spaceship\n\t5 - Boat\n\t6 - P-pentomino\n\t7 - Beacon\n\t8 - Acorn\n\t9 - Infinite\n\t10 - Glider gun\n\t11 - Github profile pic\n'))
                if not any([self.choose == x for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]):
                    raise Exception
            except Exception:
                print('You must type in an integer from the list.')
            else:
                break
        x = np.arange(0, UNIVERSE_SIZE)
        y = np.arange(0, UNIVERSE_SIZE)
        self.X, self.Y = np.meshgrid(x, y)
        self.Z = self.X + self.Y
        self.Z[:, :][:] = 0
        self.arr = np.array([])
        if self.choose == 1:
            print('Diehard')
            self.Z[70:73, 70:78][:][:] = [
                [0, 0, 0, 0, 0, 0, 1, 0],
                [1, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 1, 1],
            ]
        elif self.choose == 2:
            print('Block Switch Engine')
            self.Z[70:76, 70:78][:][:] = [
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 1, 1],
                [0, 0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0],
            ]
        elif self.choose == 3:
            print('Pentadecathlon')
            self.Z[70:73, 70:78][:][:] = [
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
            ]
        elif self.choose == 4:
            print('Spaceship')
            self.Z[70:74, 40:45][:][:] = [
                [0, 0, 1, 1, 0],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0]
            ]
        elif self.choose == 5:
            print('Boat')
            self.Z[70:73, 70:73][:][:] = [
                [1, 1, 0],
                [1, 0, 1],
                [0, 1, 0]
            ]
        elif self.choose == 6:
            print('R-pentomino')
            self.Z[40:43, 50:53][:][:] = [
                [0, 1, 1],
                [1, 1, 0],
                [0, 1, 0]
            ]
        elif self.choose == 7:
            print('Beacon')
            self.Z[70:74, 70:74][:][:] = [
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1]
            ]
        elif self.choose == 8:
            print('Acorn')
            self.Z[70:73, 110:117][:][:] = [
                [0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 1, 1, 1]
            ]
        elif self.choose == 9:
            print('Infinite')
            self.Z[70:75, 70:75][:][:] = [
                [1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 1, 1, 0, 1],
                [1, 0, 1, 0, 1],
            ]
        elif self.choose == 10:
            print('Glider gun')
            self.Z[30:39, 30:66][:][:] = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        elif self.choose == 11:
            print('Github profile pic')
            self.Z[74:86, 68:80][:][:] = [
                [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
            ]
        a = np.arange(0, SCREEN_WIDTH)
        b = np.arange(0, SCREEN_HEIGHT)
        self.A, self.B = np.meshgrid(a, b)
        self.C = self.A + self.B
        for i in range(UNIVERSE_SIZE):
            for j in range(UNIVERSE_SIZE):
                self.C[i * SCALING: (i + 1) * SCALING, j * SCALING: (j + 1)
                       * SCALING][:][:] = self.Z[i, j]
        self.surf = pg.surfarray.make_surface(self.C * 255)
        self.go = 0

    def events(self):
        """Make some seeds for the universe.
        """
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    np.savez('life_ts.npz', life=self.arr)
                    pg.quit()
                    quit()
                if event.key == pg.K_SPACE:
                    self.go += 1
                    self.go = self.go % 2
                if event.key == pg.K_r:
                    self.setup()
            if event.type == pg.QUIT:
                np.savez('life_ts.npz', life=self.arr)
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONUP and self.choose == 0:
                xx, yy = pg.mouse.get_pos()
                x, y = int(xx / SCALING), int(yy / SCALING)
                try:
                    if self.Z[:, :][:][x][y] == 1:
                        self.Z[:, :][:][x][y] = 0
                    else:
                        self.Z[:, :][:][x][y] = 1
                except Exception:
                    print('Out of bounds!')
                for i in range(UNIVERSE_SIZE):
                    for j in range(UNIVERSE_SIZE):
                        self.C[i * SCALING: (i + 1) * SCALING, j * SCALING: (j + 1)
                               * SCALING][:][:] = self.Z[i, j]
                self.surf = pg.surfarray.make_surface(self.C * 255)

    def rules(self):
        """Implement the rules of Life.
        """
        self.arr = np.r_[self.arr, np.sum(self.Z)]
        survival = np.copy(self.Z)
        nbrs_count = sum(np.roll(np.roll(self.Z[:, :][:], i, 0), j, 1)
                         for i in (-1, 0, 1) for j in (-1, 0, 1)
                         if (i != 0 or j != 0))
        for x in range(UNIVERSE_SIZE):
            for y in range(UNIVERSE_SIZE):
                if self.Z[:, :][:][x, y] == 1:
                    if nbrs_count[x, y] < 2 or nbrs_count[x, y] > 3:
                        survival[:, :][:][x, y] = 0
                elif nbrs_count[x, y] == 3:
                    survival[:, :][:][x, y] = 1
        self.Z = survival
        for i in range(UNIVERSE_SIZE):
            for j in range(UNIVERSE_SIZE):
                self.C[i * SCALING: (i + 1) * SCALING, j * SCALING: (j + 1)
                       * SCALING][:][:] = self.Z[i, j]
        self.surf = pg.surfarray.make_surface(self.C * 255)

    def game_loop(self):
        """The main loop that runs the simulation."""
        while 1:
            self.screen.fill(WHITE)
            self.screen.blit(self.surf, (0, 0))
            pg.display.update()
            self.clock.tick(FPS)
            self.events()
            if self.go:
                self.rules()


if __name__ == "__main__":
    TheGame().game_loop()
