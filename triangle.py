import numpy as np
import matplotlib.pyplot as plt


def triangle(n):
    series = []
    for i in range(n):
        add_on = np.array([(x + 1) for x in range(i)])
        series = np.concatenate((series, add_on))
    return series


A002260 = triangle(1000)
plt.figure()
plt.plot(A002260, 'o', MarkerSize=0.1)
plt.show()
