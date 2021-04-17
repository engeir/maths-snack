import time

import matplotlib.pyplot as plt
import numba as nb
import numpy as np
import pylab as pyl


@nb.njit
def mandelbrot(creal, cimag, maxiter):
    real = creal
    imag = cimag
    for n in range(maxiter):
        real2 = real * real
        imag2 = imag * imag
        if real2 + imag2 > 4.0:
            return n
        imag = 2 * real * imag + cimag
        real = real2 - imag2 + creal
    return np.NaN


@nb.njit(parallel=True)
def mandelbrot_set4(xmin, xmax, ymin, ymax, width, height, maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((height, width))
    for i in nb.prange(width):
        for j in nb.prange(height):
            n3[j, i] = np.log(mandelbrot(r1[i], r2[j], maxiter))
    return (r2, r1, n3)


t0 = time.perf_counter()
Y, X, Z = mandelbrot_set4(-2, 0.5, -1, 1, 5000, 5000, 1000)
print(time.perf_counter() - t0)

plt.imshow(
    Z,
    cmap=pyl.plt.cm.prism,
    interpolation="none",
    extent=(X.min(), X.max(), Y.min(), Y.max()),
)
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
# savefig("mandelbrot_python.svg")
plt.show()
