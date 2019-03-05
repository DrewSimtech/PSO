

# Global Package Imports
import numpy as np
from itertools import repeat
from particle import Particle


def generateStartPosition(bounds):
    pos = []
    for b in bounds:
        lower, upper = b
        sample = np.random.random_sample() * (upper - lower) + lower
        pos.append(sample)
    return pos


def particalSwarm(func, bounds, velocities, c1=2, c2=2, iterations=500, num_particles=15):
    # for each particle: init()
    particles = []
    for _ in repeat(None, num_particles):
        pos = generateStartPosition(bounds)
        print('Starting at: ' + str(pos))
        particles.append(Particle(pos, bounds, velocities, c1, c2))

    # Arrays to track 
    gBestFit = [float('inf')]
    gBestPos = []

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