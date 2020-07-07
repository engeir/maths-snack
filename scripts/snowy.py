"""Implementation of the series A279125 from OEIS.

The entry a(n) is decided by checking if n's binary value has any overlapping
with previous i=1, 2, 3, ..., n-1, also in binary. I.e., if n's binary value has
ones in places where any of the i's have ones, a(n) is the lowest integer that
has not yet been picked, i.e. a(n) > a(i) ∀ i ∈ {1, 2, 3, ..., n-1}.
"""

import numpy as np
import matplotlib.pyplot as plt

# Length of the series
size = 3000

# The series with the two first entries
A279125 = [0, 0]
# A look up table with binary numbers sorted after what entry they gave to the series
look_up = [np.zeros((2, 2))]
npad_left = ((0, 0), (1, 0))
npad_bottom = ((0, 1), (0, 0))

for n in range(3, size):
    print(f"{round(n / size * 100, 1)}%", end='\r')
    # Make a list of the digits of the binary number
    bin_list = [int(x) for x in "{:b}".format(n)]
    not_filled = True
    # Variable that decides what should be the entry of the series
    numb = 1
    # For deciding quickly if the binary number is on the form n = 2**i where i ∈\mathbb{Z}
    rest = bin_list[1:]
    if not any([int(x) for x in rest]):
        # If the number is from a power of two, it goes here, placing a '0' in the series
        A279125.append(0)
        look_up[0] = np.pad(look_up[0], pad_width=npad_left,
                            mode='constant', constant_values=0)
        look_up[0] = np.pad(look_up[0], pad_width=npad_bottom,
                            mode='constant', constant_values=0)
        look_up[0][:, -1] = bin_list
    else:
        while not_filled:
            try:
                # If the series do not yet have the entry 'numb'...
                look_up[numb]
            except Exception:
                # ... then this should be added to the look-up table
                # and the series should get 'numb' added to it
                new_entry = np.zeros((1, len(bin_list)))
                new_entry[0, :] = bin_list
                look_up.append(new_entry)
                A279125.append(numb)
                not_filled = False
            else:
                # If 'numb' is used before, we must check if the new number in binary has any overlapping '1's.
                if len(bin_list) > len(look_up[numb][0, :]):
                    diff = len(bin_list) - len(look_up[numb][0, :])
                    new_npad_left = ((0, 0), (diff, 0))
                    look_up[numb] = np.pad(
                        look_up[numb], pad_width=new_npad_left, mode='constant', constant_values=0)
                cols = [index for index, value in enumerate(bin_list) if value]
                for col in cols:
                    if any([x for x in look_up[numb][:, col]]):
                        # If there is overlapping '1's, we can't use 'numb',
                        # and we break the loop and go to the next possibility
                        break
                    if col == cols[-1]:
                        # If there are no overlapping '1's, we add the number in binary
                        # to the look-up table of 'numb' and append 'numb' to the series
                        look_up[numb] = np.pad(
                            look_up[0], pad_width=npad_bottom, mode='constant', constant_values=0)
                        look_up[numb][-1, :] = bin_list
                        A279125.append(numb)
                        not_filled = False
            numb += 1

# The list is plotted with a black background and white data points to resemble snow
plt.figure().set_facecolor('black')
plt.subplot('111', facecolor='black').tick_params(axis='x', colors='white')
plt.subplot('111', facecolor='black').tick_params(axis='y', colors='white')
plt.subplot('111', facecolor='black').spines['top'].set_color('white')
plt.subplot('111', facecolor='black').spines['bottom'].set_color('white')
plt.subplot('111', facecolor='black').spines['left'].set_color('white')
plt.subplot('111', facecolor='black').spines['right'].set_color('white')
plt.scatter(list(range(len(A279125))), A279125, s=.1, color='k', marker=',')

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

plt.savefig('snowy_hills.png', bbox_inches='tight', format='png', dpi=1200, transparent=True)
plt.show()
