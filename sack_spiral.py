"""See https://numberspiral.com for more info.
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

r = []
rr = []
t = []
tt = []
n = 0
while n < 1e6:
    if sp.isprime(n):
        r.append(np.sqrt(n))
        t.append(np.sqrt(n) * 2 * np.pi)
    else:
        rr.append(np.sqrt(n))
        tt.append(np.sqrt(n) * 2 * np.pi)
    n += 1

plt.figure()
plt.polar(tt, rr, 'o', color='grey', MarkerSize=0.1)
plt.polar(t, r, 'o', color='k', MarkerSize=0.1)
ax = plt.gca()
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.grid(False)
plt.show()
