import matplotlib.pyplot as plt

_ = None  # should delete this

A229037_lst = []  # type: list
total = 10**4

for n in range(total):
    i, j, b = 1, 1, set()
    while n - 2 * i >= 0:
        b.add(2 * A229037_lst[n - i] - A229037_lst[n - 2 * i])
        i += 1
        while j in b:
            b.remove(j)
            j += 1
            print(f"{round(n / total * 100, 1)}%", end='\r')
    A229037_lst.append(j)

plt.figure()
plt.plot(A229037_lst, 'o', markersize=1)
plt.show()
