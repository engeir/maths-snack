def cont_frac(the_number, iterations):
    """Make a list of integers that make the continued fraction of a numberself.

    Arguments:
        number {float} -- the number you want to expand into a fraction
        iterations {int} -- the length of the list of number / accurancy

    Returns:
        list -- list of the integers from most to least significant
    """
    frac_list = []
    itr = 0
    number = the_number
    while itr < iterations:
        a = int(number)
        frac_list.append(a)
        b = number - a
        try:
            number = 1 / b
        except ZeroDivisionError:
            print('The continued fraction of ' +
                  str(the_number) + ' is described perfectly by the list:')
            break
        else:
            pass
        itr += 1
    if itr == iterations:
        print('The continued fraction of ' +
              str(the_number) + '... is described in the list:')
    print(frac_list)
    return frac_list


def solve_cont_frac(liste):
    """Take in a list of integers from continued fraction-method, and find the approximation.

    Arguments:
        list {list} -- the list containing the integer values

    Returns:
        float -- the approximation extracted from the continued fraction list
    """
    rev_list = [ele for ele in reversed(liste)]
    dist = len(liste)
    for c in range(dist):
        if (c - 1) < 0:
            a = 1 / rev_list[c]
        elif (c + 1) == dist:
            a += rev_list[c]
        else:
            b = a + rev_list[c]
            a = 1 / b
    print('The continued fraction from the list equates to: ' + str(a))
    return a


try:
    # numm, precicion = float(input('Type in the float you want to find the continued fraction of and the precision (tuple), or type any character.\n'))
    numm, precicion = [float(x) for x in input("Enter two numbers here: ").split(',')]
except Exception:
    numm, precicion = 4.25, 6
h = cont_frac(numm, precicion)
numbr = solve_cont_frac(h)

phi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
n = solve_cont_frac(phi)
n = cont_frac(n, 50)

# 1.61803398875 ~ Golden ratio from Google
# 1.618033988749895 ~ Golden ratio from 'n'
