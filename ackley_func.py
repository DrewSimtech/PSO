
# Global Package Imports
from math import exp, sqrt, cos, pi, e


def ackley(pos):
    primary = 0.0
    secondary = 0.0
    for i in range(len(pos)):
        primary   += pos[i] * pos[i]
        secondary += cos(2.0 * pi * pos[i])
    ackley_prime  = exp(-0.2 * sqrt(0.5 * primary))
    ackley_second = exp( 0.5 * secondary)
    ackley = -20.0 * ackley_prime - ackley_second + e + 20.0
    return ackley