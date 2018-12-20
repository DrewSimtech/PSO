
# Local Package Imports
from pso import particalSwarm
from ackley_func import ackley
import plot


def main():
    start_pos = [ 2,  -4]
    bounds    = [10, -10]
    best_fit = particalSwarm(ackley, start_pos, bounds)
    plot.plotPositions(best_fit[-1])
    #plot.plotVelocities(best_fit[-1])
    plot.plotFitness(best_fit[-1])
    #plot.plotHeightColorMap(best_fit[-1])
    plot.plotTimeColorMap(best_fit[-1])
    plot.show()


if __name__ == '__main__':
    main()