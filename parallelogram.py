import matplotlib.pyplot as plt
import itertools


def erat2():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x & 1):
                x += p
            D[x] = p


def get_primes_erat(n):
    return list(itertools.takewhile(lambda p: p < n, erat2()))


def parallelograms(how_big):
    aa = []
    a = get_primes_erat(how_big)
    for n in a:
        org, rev = int("{:b}".format(n), 2), int('{:b}'.format(n)[::-1], 2)
        # n += 1
        m = org - rev
        aa.append(m)
        # print(n, m)
    return aa


aa = parallelograms(262000)  # 30000

plt.figure(figsize=(16, 9))
plt.scatter(list(range(len(aa))), aa, s=0.1, c='k')

# Remove labels, axes etc.
spines = ["top", "right", "left", "bottom"]
for sp in spines:
    plt.gca().spines[sp].set_visible(False)
plt.tick_params(axis='y', which='both', left=False,
                right=False, labelleft=False)
plt.tick_params(axis='x', which='both', bottom=False,
                top=False, labelbottom=False)
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])

# plt.savefig('parallelogram.pdf', bbox_inches='tight', format='pdf', dpi=600)
plt.show()
