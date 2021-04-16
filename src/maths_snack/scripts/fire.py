import matplotlib.pyplot as plt

_ = None  # should delete this

A229037_lst = []  # type: list
total = 10 ** 4
# total = 10**4

for n in range(total):
    i, j, b = 1, 1, set()
    while n - 2 * i >= 0:
        b.add(2 * A229037_lst[n - i] - A229037_lst[n - 2 * i])
        i += 1
        while j in b:
            b.remove(j)
            j += 1
            print(f"{round(n / total * 100, 1)}%", end="\r")
    A229037_lst.append(j)

f = plt.figure()
plt.plot(A229037_lst, "o", markersize=1, color=(0.745, 0.0, 0.094))

# Remove labels, axes etc.
spines = ["top", "right", "left", "bottom"]
for sp in spines:
    plt.gca().spines[sp].set_visible(False)
plt.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)
plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
COLOR = (0.2, 0.2, 0.2)
plt.gca().set_facecolor(COLOR)
f.patch.set_facecolor(COLOR)

# plt.savefig('fire.png', bbox_inches='tight', format='png', dpi=600)
plt.show()
