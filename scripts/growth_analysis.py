import numpy as np
import matplotlib.pyplot as plt


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

logi = lambda x: 4. * x * (1 - x)

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
