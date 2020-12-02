import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random


# rate_change = 0.001
rate_change = 0.00001

def final_pop(r):
    n = [0.5]
    for _ in range(40):
        n.append(r * n[-1] * (1 - n[-1]))
        if len(n) > 10:
            n.pop(0)
    return n[random.randint(0, 9)]

def final_put(r):
    n = [0.5]
    for _ in range(40):
        n.append(r * n[-1] * (1 - n[-1]))
        if len(n) > 10:
            n.pop(0)
    return n

def chaos(r_max):
    r = []
    m = []
    rate = 2.8
    while rate < r_max:
        if rate < 3.4:
            r = np.r_[r, rate]
            m = np.r_[m, final_pop(rate)]
            # m.append(final_pop(rate))
        else:
            r = np.r_[r, [rate for _ in range(10)]]
            m = np.r_[m, final_put(rate)]
            # m.append(final_put(rate))
        rate += rate_change
    return list(r),  list(m)

rates, chaotic = chaos(4.)
x_min = rates[0]  # - len(chaotic) / 10
x_max = rates[-1]  # len(chaotic) * rate_change  # + len(chaotic) / 10
y_min = 0  # min(chaotic) - max(chaotic) / 10
y_max = 1  # max(chaotic) + max(chaotic) / 10
data = np.zeros((len(chaotic), 2))
data[:, 0] = rates  # [x * rate_change for x in range(len(chaotic))]
data[:, 1] = chaotic


if rate_change < 0.001:
    plt.figure()
    plt.plot(rates, chaotic, 'o', markersize=1)
    # plt.plot([x * rate_change for x in range(len(chaotic))],
    #         chaotic, 'o', markersize=1)
    plt.show()
else:
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'ro', markersize=1)


    def init():
        plt.xlabel('Growth Rate')
        spines = ["top", "right", "left", "bottom"]
        for sp in spines:
            plt.gca().spines[sp].set_visible(False)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        return ln,


    def update(frame):
        x, y = frame
        xdata.append(x)
        ydata.append(y)
        ln.set_data(xdata, ydata)
        return ln,


    ani = FuncAnimation(fig, update, frames=data, interval=1,
                        init_func=init, blit=True)

    # ani.save('growth.gif', writer='imagemagick', fps=60)

    plt.show()
