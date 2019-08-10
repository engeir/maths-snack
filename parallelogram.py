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


aa = parallelograms(30000)

plt.figure()
plt.scatter([x for x in range(len(aa))], aa, s=0.4)
plt.show()
