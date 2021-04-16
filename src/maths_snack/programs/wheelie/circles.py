import numpy as np
import pygame as pg
import scipy.signal as sig

import maths_snack.programs.wheelie.config as cf


class Circle:
    """Make a times table calculation."""

    def __init__(self):
        self.radius = cf.RADIUS
        self.last_x = None
        self.last_y = None

    def draw(self, screen, wheels, theta, draw, version):
        x0, y0 = int(cf.SCREEN_WIDTH * 0.75), int(
            cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * 0.04
        )
        # Normalize radius
        r_tot = np.einsum("ij->j", wheels)[0]
        r_scale = self.radius / r_tot
        wheels[:, 0] = wheels[:, 0] * r_scale
        # Normalize speed
        v_max = np.max(wheels[:, 1])
        if version == "w0":
            v_limit = 15
        else:
            v_limit = 5
        v_scale = v_limit / v_max
        wheels[:, 1] = wheels[:, 1] * v_scale
        x = np.array([x0])
        y = np.array([y0])
        for w in wheels:
            r, omega, offset = w[0], w[1], w[2]
            pg.draw.circle(
                screen, cf.R7, (int(x[-1] - cf.SCREEN_WIDTH * 0.5), int(y[-1])), r, 1
            )
            x_ = int(r * np.cos(theta * omega + offset)) + x[-1]
            y_ = int(r * np.sin(theta * omega + offset)) + y[-1]
            x = np.r_[x, x_]
            y = np.r_[y, y_]
            p = np.c_[x - int(cf.SCREEN_WIDTH * 0.5), y]
            pg.draw.lines(screen, cf.WHITE, False, p, 1)
        if self.last_x is not None:
            if draw:
                try:
                    pg.draw.line(
                        screen, cf.WHITE, (self.last_x, self.last_y), (x[-1], y[-1]), 4
                    )
                except Exception:
                    pass
        self.last_x = x[-1]
        self.last_y = y[-1]


class Wheel:
    def __init__(self):
        self.first = True
        self.x = np.array([])
        self.y = np.array([])
        self.path = np.array([])
        self.w = None
        self.rad = int(cf.SCREEN_HEIGHT / 2 - cf.SCREEN_HEIGHT * 0.1)
        self.ell = cf.SCREEN_WIDTH / 2 - self.rad
        self.r = cf.SCREEN_WIDTH / 2 + self.rad
        self.t = cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * 0.05 - self.rad
        self.b = cf.SCREEN_HEIGHT / 2 + cf.SCREEN_HEIGHT * 0.05 + self.rad
        self.p = [
            (self.ell, self.t),
            (self.r, self.t),
            (self.r, self.b),
            (self.ell, self.b),
        ]

    def create_wheel(self, wheel):
        if wheel == "w1":
            w1 = np.array([[1, -2 / 4, 0], [0.5, 5 / 4, 0], [1 / 4, 19 / 4, 0]])
            self.w = w1
        elif wheel == "w2":
            w2 = np.array(
                [
                    [1, 0.8, 0.4, 0.2, 0.4, 0.2],
                    [1, 10, -17, -26, 28, 37],
                    [0, -np.pi / 2, -np.pi / 2, 0, 0, np.pi / 2],
                ]
            ).T
            self.w = w2
        elif wheel == "w3":
            w3 = np.array([[1, 1 / 2, 1 / 4], [1, 4, 31], [0, 0, 0]]).T
            self.w = w3
        elif wheel == "w4":
            w4 = np.array([[1, 1 / 2, 1 / 4], [1, 3, 80], [0, 0, 0]]).T
            self.w = w4
        elif wheel == "w5":
            w5 = np.array(
                [
                    [1, 0.4, 0.3, 0.3, 0.1, 0.05],
                    [1, 3, 5, -10, 3, 45],
                    [0, np.pi, 0, np.pi / 2, 0, 0],
                ]
            ).T
            self.w = w5
        if wheel == "w0":
            pass
        else:
            self.order()

    def draw_path(self, screen, x, y, pressed=False):
        pg.draw.lines(screen, cf.WHITE, True, self.p, 1)
        if pressed:
            if (self.ell < x < self.r) and (self.t < y < self.b):
                self.x = np.r_[self.x, x]
                self.y = np.r_[self.y, y]
                self.path = np.c_[self.x, self.y]
        try:
            pg.draw.lines(screen, cf.WHITE, False, self.path, 1)
        except Exception:
            pass

    def remove_adjacent(self):
        i_last = None
        j_last = None
        c = 1
        for i, j in self.path[:-5, :]:
            if i_last is None and j_last is None:
                i_last = i
                j_last = j
            else:
                dist = abs(
                    (i * i + j * j) ** 0.5 - (i_last * i_last + j_last * j_last) ** 0.5
                )
                if dist < 3:
                    self.x = np.delete(self.x, c)
                    self.y = np.delete(self.y, c)
                else:
                    c += 1
                    i_last = i
                    j_last = j

    def f_trans(self):
        if self.first:
            self.remove_adjacent()
            # self.smooth()
            self.first = False
        signal = self.x + 1j * self.y
        fourier = np.fft.fft(signal)
        n = signal.size
        radiuses = np.abs(fourier)
        freqs = np.fft.fftfreq(n)
        phases = np.angle(fourier)
        self.w = np.c_[radiuses, freqs, phases]
        self.order()
        try:
            self.w = self.w[1:51, :]
        except Exception:
            pass

    def smooth(self):
        # print(type(self.x))
        # self.x = pd.Series(self.x).rolling(window=7).mean()
        # print(type(self.x))
        # self.y = pd.Series(self.y).rolling(window=7).mean()
        N = 3
        Wn = 0.9
        B, A = sig.butter(N, Wn, output="ba")
        self.x = sig.filtfilt(B, A, self.x)
        self.y = sig.filtfilt(B, A, self.y)
        # w_len = 21
        # out_x = np.r_[self.x[w_len - 1:0:-1], self.x, self.x[-2:- w_len - 1:- 1]]
        # out_y = np.r_[self.y[w_len - 1:0:-1], self.y, self.y[-2:- w_len - 1:- 1]]
        # # window = eval('np.blackman(11)')

        # window = np.ones(10)
        # self.x = np.convolve(window / window.sum(), out_x, mode='valid')
        # self.y = np.convolve(window / window.sum(), out_y, mode='valid')

    def order(self):
        self.w = self.w[self.w[:, 0].argsort(), :][::-1]
