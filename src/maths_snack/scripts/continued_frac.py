import decimal as dc

dc.getcontext().prec = 123  # 123 decimal precision


def cont_frac(the_number: float, iterations: int) -> list:
    """Make a list of integers that make the continued fraction of a numberself.

    Args:
        the_number: the number you want to expand into a fraction
        iterations: the length of the list of number / accurancy

    Returns:
        list: list of the integers from most to least significant
    """
    frac_list: list[int] = []
    itr = 0
    number = dc.Decimal(the_number)
    while itr < iterations:
        a = int(number)
        frac_list.append(a)
        b = number - a
        try:
            number = 1 / b
        except ZeroDivisionError:
            print(
                "The continued fraction of "
                + str(the_number)
                + " is described perfectly by the list:"
            )
            break
        else:
            pass
        itr += 1
    if itr == iterations:
        print(
            "The continued fraction of "
            + str(the_number)
            + "... is described in the list:"
        )
    print(frac_list)
    _ = solve_cont_frac(frac_list)
    type_numb = most_frequent(frac_list)
    threshold = -1
    for i, numb in enumerate(frac_list):
        if numb > 100 * type_numb:
            threshold = i
            break
    approx = frac_list[:threshold]
    # Highest number, but this becomes silly when two VERY large numbers are
    # found, and the one that is somewhat larger is far down the list.
    # approx = frac_list[:frac_list.index(max(frac_list))]
    print(f"A good approximation would therefore be:\n{approx}")
    _ = solve_cont_frac(approx)
    return frac_list


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num


def solve_cont_frac(liste: list) -> dc.Decimal:
    """Take in a list of integers from continued fraction-method, and find the approximation.

    Args:
        liste: the list containing the integer values

    Returns:
        float: the approximation extracted from the continued fraction list
    """
    rev_list = [ele for ele in reversed(liste)]
    dist = len(liste)
    a: dc.Decimal = dc.Decimal(0)
    for c in range(dist):
        if (c - 1) < 0:
            a = dc.Decimal(1 / rev_list[c])
        elif (c + 1) == dist:
            a += dc.Decimal(rev_list[c])
        else:
            b = a + rev_list[c]
            a = dc.Decimal(1 / b)
    print("The continued fraction from the list equates to: " + str(a))
    return a


try:
    # numm, precicion = float(input('Type in the float you want to find the continued fraction of and the precision (tuple), or type any character.\n'))
    numm, precicion = [float(x) for x in input("Enter two numbers here: ").split(",")]
    print(f"Okay, expanding {numm} using {precicion} continued fractions.")
except Exception:
    numm, precicion = 4.25, 6
h = cont_frac(numm, int(precicion))
# numbr = solve_cont_frac(h)

# phi = [
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
# ]
# n = solve_cont_frac(phi)
# _ = cont_frac(n, 50)

# 1.61803398875 ~ Golden ratio from Google
# 1.618033988749895 ~ Golden ratio from 'n'
