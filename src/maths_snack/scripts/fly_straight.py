import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

length = 900


def fly_straight(how_big):
    n = 2
    a = [1, 1]
    while n < how_big:
        a.append(find_next(a[-1], n))
        n += 1

    return a


def find_next(a, n):
    if math.gcd(a, n) == 1:
        c = a + n + 1
    else:
        c = a / (math.gcd(a, n))
    return int(c)


aa = fly_straight(length)
x_min = -len(aa) / 10
x_max = len(aa) + len(aa) / 10
y_max = max(aa) + max(aa) / 10
y_min = min(aa) - max(aa) / 10
data = np.zeros((len(aa), 2))
data[:, 0] = [x for x in range(len(aa))]
data[:, 1] = aa


fig, ax = plt.subplots()
xdata, ydata = [], []
(ln,) = plt.plot([], [], "ro", markersize=1)


def init():
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    return (ln,)


def update(frame):
    x, y = frame
    xdata.append(x)
    ydata.append(y)
    ln.set_data(xdata, ydata)
    return (ln,)


ani = FuncAnimation(fig, update, frames=data, interval=10, init_func=init, blit=True)

# Remove labels, axes etc.
spines = ["top", "right", "left", "bottom"]
for sp in spines:
    plt.gca().spines[sp].set_visible(False)
plt.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)
plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])

# ani.save('fly_straith.gif', writer='imagemagick', fps=60)

plt.show()
