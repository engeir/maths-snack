import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ssi


def est_pdf(signal):
    """Estimate the PDF of `signal`.
    Args:
        signal (np.ndarray): the signal that is analysed
    """
    # bins = np.linspace(-5, 5, 30)
    histogram, bins = np.histogram(signal, bins=1000, density=True)
    bin_centers = 0.5*(bins[1:] + bins[:-1])
    # Compute the PDF on the bin centers from scipy distribution object
    # norm_pdf = stats.norm.pdf(bin_centers)
    return bin_centers, histogram


def est_psd(signal):
    Xn = (signal - signal.mean()) / signal.std()
    plt.figure()
    plt.plot(Xn)
    fp, P_Xn = ssi.periodogram(Xn)
    f, S_Xn = ssi.welch(Xn, nperseg=2**10)
    plt.figure()
    plt.loglog(fp[1:], P_Xn[1:])
    plt.loglog(f[1:], S_Xn[1:])
    plt.show()


def growth():
    def logi(x): return 4. * x * (1 - x)

    arr = np.array([])

    # Initialize with some number...
    x = np.random.rand()
    print(x)
    while len(arr) < 1e5:
        x = logi(x)
        arr = np.r_[arr, x]

    x, y = est_pdf(arr)
    plt.figure()
    plt.plot(arr, 'o')
    plt.figure()
    plt.plot(x, y)
    plt.show()


def life():
    f = np.load('life_ts_gh-profile.npz')
    life_ts = f['life']
    est_psd(life_ts)


if __name__ == '__main__':
    # growth()
    life()
