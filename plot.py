
# Global package imports
import numpy as np
import matplotlib.pyplot as plt
# Local package imports
from particle import Particle


def plotPositions(particles):
    plt.figure()
    plt.grid()
    for p in particles:
        pos = p.getPositions()
        plt.plot(pos[0], pos[1])
        plt.xlabel('pos x')
        plt.ylabel('pos y')

def plotVelocities(particles):
    for d in range(particles[0].getDimentions()):
        plt.figure()
        plt.grid()
        for p in particles:
            vel = p.getVelocities()
            plt.plot(vel[d])
            plt.ylabel('vel ' + str(d))

def plotFitness(particles):
    plt.figure()
    plt.grid()
    for p in particles:
        fit = p.getFitness()
        plt.plot(fit)
        plt.ylabel('fitness')
    plt.figure()
    plt.grid()
    for p in particles:
        fit = p.getBestFitness()
        plt.plot(fit)
        plt.ylabel('best fitness')

def plotHeightColorMap(particles):
    for p in particles:
        plt.figure()
        plt.grid()
        pos = p.getPositions()
        fit = np.array(p.getFitness())
        plt.scatter(pos[0], pos[1], c=fit, cmap='gray')
        plt.xlabel('pos x')
        plt.ylabel('pos y')

def plotTimeColorMap(particles):
    for p in particles:
        plt.figure()
        plt.grid()
        pos = p.getPositions()
        time = np.flip(np.array(range(len(pos[0]))),0)
        plt.scatter(pos[0], pos[1], c=time, cmap='gray')
        plt.xlabel('pos x')
        plt.ylabel('pos y')

def scatterTest():
    plt.figure()
    plt.grid()
    n = 50
    x = np.random.rand(n)
    y = np.random.rand(n)
    c = np.random.rand(n)
    plt.scatter(x, y, c=c)

def show():
    plt.show()