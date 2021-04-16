import matplotlib.pyplot as plt


def van_eck(the_end: int):
    """Make the van Eck-sequence.

    The first entry is a(0) = 0. At a(n+1) you then ask weather you have seen a(n) before,
    if no, a(n+1) = 0, if yes a(n+1) is equal to the amount of steps we must
    take to get to the last time we saw a(n). For a(1), we have not seen a(0)=0 before, so a(1) = 0.
    At a(2) we have seen a(1) = 0 before [a(0) is also 0], and it was one step backwards, so a(2) = 1.

    Args:
        the_end: how many entries we want to compute for the series

    Returns:
        list -- the series presented as a list
    """
    c = 0
    series = [0]
    while c < the_end:
        if series[-1] in series[:-1]:
            series.append(list(reversed(series[:-1])).index(series[-1]) + 1)
        else:
            series.append(0)
        c += 1
    return series


a = van_eck(10000)
plt.figure("The Van Eck Sequence")
plt.plot(list(range(len(a))), a)
plt.xlabel("Van Eck sequence index")
plt.ylabel("Number")
plt.show()
