import math
import random


def in_circle(x: float, y: float, radius: float = 1):
    """Return True if the point is in the circle and False otherwise.

    Args:
        x: x position
        y: y position
        radius: radius of the circle

    Returns:
        bool: If the point is inside the circle or not
    """
    return (x ** 2 + y ** 2) < radius * radius


def monte_carlo(n_samples: int, radius: float = 1):
    """Return the estimate of pi using the monte carlo algorithm.

    Args:
        n_samples: number of samples used for the MC estimation
        radius: the radius of the circle

    Returns:
        float: Estimate of pi
    """
    in_circle_count = 0
    for i in range(n_samples):

        # Sample x, y from the uniform distribution
        x = random.uniform(0, radius)
        y = random.uniform(0, radius)

        # Count the number of points inside the circle
        if in_circle(x, y, radius):
            in_circle_count += 1

    # Since we've generated points in upper left quadrant ([0,radius], [0, radius])
    # We need to multiply the number of points by 4
    pi_estimate = 4 * in_circle_count / (n_samples)

    return pi_estimate


if __name__ == "__main__":

    pi_estimate = monte_carlo(1000000)
    percent_error = 100 * abs(math.pi - pi_estimate) / math.pi

    print("The estimate of pi is: {:.3f}".format(pi_estimate))
    print("The percent error is: {:.3f}".format(percent_error))
