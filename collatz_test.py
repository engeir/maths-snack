from itertools import cycle

import matplotlib.pyplot as plt
import numpy as np

import collatz as co


def rotating_line(series):
    l = np.asarray([[0, 0], [0, 1]])
    a = .05
    for s in series:
        if s == 0:
            phi = - a
        elif s == 1:
            phi = a
        else:
            phi = 0
        last = l[0, -1] + 1j * l[1, -1]
        i = l[0, -1] - l[0, -2] + 1j * (l[1, -1] - l[1, -2])
        new = i * (np.real(np.exp(1j * phi)) + 1j * np.imag(np.exp(1j * phi))) + last
        l = np.c_[l, [np.real(new), np.imag(new)]]
    return l


c = cycle(['#B2FF66', '#66FF66', '#FFB266',
           '#FF9933', '#994C00', '#FF6666',
           '#990000', '#FF9999', '#003300'])
plt.figure()
for n in range(1, int(1e4)):
    c_series = co.collatz(n, list_out=True)
    line = rotating_line(c_series)
    plt.plot(line[0, 3:], line[1, 3:], next(c), alpha=.2, linewidth=3)
plt.show()
