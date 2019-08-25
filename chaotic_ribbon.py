import matplotlib.pyplot as plt

A055748 = [0, 1, 1]

size = 1000000

for i in range(3, size):
    n_1 = A055748[i - 1]
    n_2 = A055748[i - 2]
    first_term = A055748[n_1]
    second_term = A055748[i - n_2 - 1]
    A055748.append(first_term + second_term)

A055748.pop(0)

plt.figure()
plt.plot(A055748, 'o', MarkerSize=1)
plt.show()
