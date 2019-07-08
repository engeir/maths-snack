import matplotlib.pyplot as plt


def van_eck(the_end):
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
plt.figure('The Van Eck Sequence')
plt.plot(list(range(len(a))), a)
plt.xlabel('Van Eck sequence index')
plt.ylabel('Number')
plt.show()


for i in range(10):
    print(i**2)
