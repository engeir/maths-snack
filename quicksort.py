import random
import pygame as pg
import asyncio
import time

# CONSTANTS
FPS = 30
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
ARRAY_LENGTH = 100
WIDTH = int(SCREEN_WIDTH / ARRAY_LENGTH)


class QuickSort:
    """Make an array and a method for sorting it."""

    def __init__(self):  # , screen, arr):
        pass
        # self.disp = screen
        # self.liste = arr
        # self.count = 0
        # self.arr = [random.randrange(1, 700, 1) for n in range(ARRAY_LENGTH)]
        # self.screen = False

    # def draw(self):
        # x_pos = 0
        # for array in self.arr:
        #     pg.draw.rect(self.screen, (255, 255, 255), (x_pos, 750, WIDTH, -array))
        #     x_pos += WIDTH

    # async def do_all(self, screen, arr, start, end):
    #     # await self.draw(screen, arr)
    #     # loop = asyncio.get_event_loop()
    #     # loop.run_until_complete(self.sort.do_all(self.screen,
    #     #                                             self.arr, 0, len(self.arr) - 1))
    #     # loop.run_until_complete(self.quick_sort(arr, 0, len(arr) - 1))
    #     # loop.close()
    #     # await self.quick_sort(arr, start, end)
    #     await asyncio.wait([self.draw(screen, arr), self.quick_sort(arr, start, end), self.draw(screen, arr), self.draw(screen, arr)])

    def draw(self, screen, arr):
        # await asyncio.sleep(0.000001)
        # x_pos = 0
        # for array in self.liste:
        #     pg.draw.rect(self.disp, (255, 255, 255),
        #                  (x_pos, 750, WIDTH, -array))
        #     x_pos += WIDTH
        # print(2)
        # screen.fill((20, 2, 2))
        x_pos = 0
        for array in arr:
            pg.draw.rect(screen, (255, 255, 255),
                         (x_pos, 750, WIDTH, -array))
            x_pos += WIDTH

    # def sort_it(self, arr):
    #     self.quick_sort(arr, 0, len(arr) - 1)
        # self.screen = screen

    def quick_sort(self, array, start, end):
        if start >= end:
            return

        index = self.partition(array, start, end)
        self.quick_sort(array, start, index - 1)
        self.quick_sort(array, index + 1, end)

    def partition(self, array, start, end):
        pivotIndex = start
        pivotValue = array[end]
        i = start
        while i < end:
            if array[i] < pivotValue:
                self.swap(array, i, pivotIndex)
                pivotIndex += 1
            i += 1

        self.swap(array, pivotIndex, end)
        return pivotIndex

    def swap(self, array, a, b):
        temp = array[a]
        array[a] = array[b]
        array[b] = temp
        # if self.screen:
        #     self.draw()

    # async def sleep(self, ms):
    #     return Promise(resolve => setTimeout(resolve, ms))


class Sim:
    """Simulate the sorting."""

    def __init__(self):
        pg.init()
        self.FPS = FPS
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.screen = pg.display.set_mode(
            (self.screen_width, self.screen_height))
        pg.display.set_caption('Quick Sort')
        self.clock = pg.time.Clock()
        self.arr = None
        self.setup()
        # self.a = 0

    def setup(self):
        self.arr = [random.randrange(1, 700, 1) for n in range(ARRAY_LENGTH)]
        self.sort = QuickSort()  # self.screen, self.arr)
        self.screen.fill((20, 2, 2))

    def events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    self.setup()
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    def sim_loop(self):
        while 1:
            self.screen.fill((20, 2, 2))
            self.sort.draw(self.screen, self.arr)
            # loop = asyncio.get_event_loop()
            # loop.run_until_complete(self.sort.do_all(self.screen,
            #                                          self.arr, 0, len(self.arr) - 1))
            # loop.run_until_complete(self.sort.quick_sort(
            #     self.arr, 0, len(self.arr) - 1))
            # loop.close()
            # self.sort.do_all(self.screen,
            #                  self.arr, 0, len(self.arr) - 1)
            self.sort.quick_sort(self.arr, 0, len(self.arr) - 1)
            # self.sort.sort_it(self.arr)
            pg.display.update()
            self.clock.tick(self.FPS)
            self.events()
            # print(1)


if __name__ == "__main__":
    Sim().sim_loop()
