"""Look at the structures in the plot. Closely.
Then you might see some chapels emerging.
"""

import matplotlib.pyplot as plt
import numpy as np


def triangle(n):
    series = []
    for i in range(n):
        add_on = np.array([(x + 1) for x in range(i)])
        series = np.concatenate((series, add_on))
    return series


A002260 = triangle(1000)
plt.figure()
plt.plot(A002260, "o", MarkerSize=0.1, marker=",")

# Remove labels, axes etc.
spines = ["top", "right", "left", "bottom"]
for sp in spines:
    plt.gca().spines[sp].set_visible(False)
plt.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)
plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])

plt.show()
