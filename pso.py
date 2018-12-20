

# Global Package Imports
import numpy as np
from itertools import repeat
from particle import Particle


def generateStartPosition(bounds, dimentions):
    lower = bounds[0]
    upper = bounds[1]
    pos = []
    for _ in repeat(None, dimentions):
        sample = np.random.random_sample() * (upper - lower) + lower
        pos.append(sample)
    return pos


def particalSwarm(func, start_pos, bounds, iterations=500, num_particles=15, c1=2, c2=2):
    gBestFit = [float('inf')]
    gBestPos = [start_pos]

    # for each particle: init()
    dimentions = len(start_pos)
    # first particle init at starting pos. generate the rest
    particles = [Particle(start_pos, c1, c2)]
    for _ in repeat(None, num_particles - 1):
        pos = generateStartPosition(bounds, dimentions)
        print('Starting at: ' + str(pos))
        particles.append(Particle(pos, c1, c2))

    # for each iteration: update particle
    for _ in repeat(None, iterations):
        # for each particle: calculate fitness
        curBestPos = (float('inf'), float('inf'))
        curBestFit = float('inf')
        for p in range(num_particles):
            fitness, pos = particles[p].checkFitness(func)
            #print('fit: ' + str(fitness))
            if(curBestFit > fitness):
                #print(' #####  NEW BEST FIT  #####\npos: ' + str(pos) + '\n #####  NEW BEST FIT  #####')
                curBestPos = pos
                curBestFit = fitness
        print('gBest({0}) > curBestFit({1})'.format(gBestFit[-1], curBestFit))
        if(gBestFit[-1] > curBestFit):
            print('bump')
            gBestPos.append(curBestPos)
            gBestFit.append(curBestFit)
        else:
            gBestPos.append(gBestPos[-1])
            gBestFit.append(gBestFit[-1])

        # for each particle: update velocity, then update position
        for p in range(num_particles):
            particles[p].updateVelocity(gBestPos)
            particles[p].updatePosition()

    print('gBestFit: {0}\ngBestPos: {1}'.format(gBestFit[-1], gBestPos[-1]))
    return gBestFit, particles