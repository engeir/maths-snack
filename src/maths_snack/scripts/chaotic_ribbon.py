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
plt.plot(A055748, "o", MarkerSize=1, color=(0.7, 0.2, 0.2))

# Remove labels, axes etc.
spines = ["top", "right", "left", "bottom"]
for sp in spines:
    plt.gca().spines[sp].set_visible(False)
plt.tick_params(axis="y", which="both", left=False, right=False, labelleft=False)
plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])

# plt.savefig('chaotic_ribbon.png', bbox_inches='tight', format='png', dpi=600, transparent=True)
plt.show()
