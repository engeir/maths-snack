from itertools import cycle

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

import collatz as co


# === SETTINGS ===
# Fav
COLOR = (0.26, .4, .49)
c = cycle(['#B2FF66', '#66FF66', '#FFB266',
           '#FF9933', '#994C00', '#FF6666',
           '#990000', '#FF9999', '#003300'])
n_mx = int(1e4)
# Other
# COLOR = (0, 0, 0)
# c = cycle([(i, i, i) for i in np.linspace(.3, 1, 9)])
# n_mx = int(1e4)

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


# pdffig = PdfPages('collatz_sea_weed_5.pdf')
f = plt.figure()
sub = f.add_subplot(1, 1, 1)
for n in range(1, n_mx):
    c_series = co.collatz(n, list_out=True)
    line = rotating_line(c_series)
    plt.plot(line[0, 3:], line[1, 3:], color=next(c), alpha=.2, linewidth=3)
plt.axis('off')
sub.set_facecolor(COLOR)
f.patch.set_facecolor(COLOR)
plt.tight_layout()
# plt.savefig('collatz_sea_weed_trans.png', bbox_inches='tight', format='png', dpi=600)
# pdffig.close()
plt.show()
