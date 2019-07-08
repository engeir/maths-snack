#!/usr/bin/env python
import matplotlib.pyplot as plt

# %%


def collatz(num):
    count = 0
    while not num == 1:
        # print(num)
        count += 1
        if num % 2:
            num = (3 * num + 1) / 2
            count += 1
        else:
            num /= 2
    return count


# Record below 100 million: 63 728 127
tall = collatz(63728127)
print(tall)
# %%
rec = 0
start = 1
end = start + 1000000
diff = end - start

# %%
n_list = []
tall_list = []
for n in range(start, end, 2):
    tall = collatz(n)
    n_list.append(n)
    tall_list.append(tall)
    if tall > rec:
        rec = tall
        # print(rec, n)
# %%
plt.figure()
plt.scatter(n_list, tall_list, s=0.1)
plt.xlabel('Input number')
plt.ylabel('Number of steps to 1')
plt.show()
