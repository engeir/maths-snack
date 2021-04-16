gonal_number = int(input("What shape/gonal number do you want? "))
h_c = 2
pyr_c = 1
h = 1
pyr = 0
awsm_list = []


def hept_pyramid(s: int, n: int) -> int:
    """Make a pyramid with a polygonal shaped base.

    Args:
        s: polygonal shape
        n: height/side length of the pyramid

    Returns:
        int: number of canon balls needed to make the pyramid
    """
    pyramid = (3 * n ** 2 + n ** 3 * (s - 2) - n * (s - 5)) / 6
    return int(pyramid)


def hept(s: int, n: int) -> int:
    """Make a polygon of aritrary gonal number and side length.

    Arguments:
        s: polygonal shape
        n: side length of the polygon

    Returns:
        int: number of canon balls needed to make the polygon
    """
    heptagon = (n ** 2 * (s - 2) - n * (s - 4)) / 2
    return int(heptagon)


try:
    while True:
        if h == pyr:
            print(
                "Success! Gonal number = "
                + str(gonal_number)
                + " Pyramid count = "
                + str(pyr_c)
                + " Polygon count = "
                + str(h_c)
                + " Canon balls = "
                + str(h)
            )
            awsm_list.append([gonal_number, pyr_c, h_c, h])
            pyr_c += 1
            pyr = hept_pyramid(gonal_number, pyr_c)
        elif h < pyr:
            h_c += 1
            h = hept(gonal_number, h_c)
        elif h > pyr:
            pyr_c += 1
            pyr = hept_pyramid(gonal_number, pyr_c)
        if pyr_c > 5000:
            gonal_number += 1
            h_c = 2
            pyr_c = 1
            h = 1
            pyr = 0
except KeyboardInterrupt:
    pass

print("\nHere is the awsm list!", str(awsm_list))
