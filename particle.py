

# Global Package Imports
import numpy as np


class Particle(object):

    ###################################
    # INITIALIZATION                  #
    ###################################
    def __init__(self, pos, bounds, c1, c2):
        # setup position and velocity arrays
        self._pos = [pos]
        self._bounds = bounds
        self._dim = len(pos)
        self._vel = [[np.random.random_sample() for x in pos]]
        # setup velocity extreems
        self._vmin = -1.0
        self._vmax = 1.0
        # setup local fitness arrays
        self._pBestFit = [float('inf')]
        self._pBestPos = [pos]
        self._fit   = [float('inf')]
        # setup learning factors
        self._c1 = c1
        self._c2 = c2

    ###################################
    # UPDATES                         #
    ###################################
    def checkFitness(self, func):
        '''Calculate Fitness function:
        current fitness = func(p os)
        if cur_fit better than pBest: pBest = cur_fit'''
        fitness = func(self._pos[-1])
        best = self._pos[-1] if self._pBestFit[-1] > fitness else self._pBestPos[-1]
        self._pBestPos.append(best)
        self._pBestFit.append(fitness if self._pBestFit[-1] > fitness else self._pBestFit[-1])
        self._fit.append(fitness)
        return fitness, self._pos[-1]
    
    def updateVelocity(self, gBest):
        '''Velocity update function:
        v[] += c1 * rand(0,1) * (pBest - Pos) + c2 * rand(0,1) * (gBest - Pos)'''
        # pVel = c1 * rand(0,1) * (pBest - Pos)
        l_factor1 = self._c1 * np.random.random_sample()
        pVel = np.subtract(self._pBestPos[-1], self._pos[-1])
        pVel = np.multiply(l_factor1, pVel)
        # gVel = c2 * rand(0,1) * (gBest - Pos)
        l_factor2 = self._c2 * np.random.random_sample()
        gVel = np.subtract(gBest[-1], self._pos[-1])
        gVel = np.multiply(l_factor2, gVel)
        # dVel = pVel + gVel
        dVel = np.add(pVel, gVel)
        # v[] += dVel
        nVel = np.add(self._vel[-1], dVel)
        # clamp velocities to prevent them from getting out of hand.
        nVel = np.clip(nVel, self._vmin, self._vmax)
        # store it. 
        self._vel.append(nVel)            
    
    def updatePosition(self):
        '''Position update function:
        Pos += Vel'''
        self._pos.append(np.add(self._pos[-1], self._vel[-1]))

    ###################################
    # LIST ACCESSORS                  #
    ###################################
    def getDimentions(self):
        return self._dim

    def getPositions(self):
        ordered_pos = []
        for d in range(self._dim):
            ordered_pos.append([])
        for p in self._pos:
            for d in range(self._dim):
                ordered_pos[d].append(p[d])
        return ordered_pos
    
    def getVelocities(self):
        velocities = []
        for d in range(self._dim):
            velocities.append([])
        for v in self._vel:
            for d in range(self._dim):
                velocities[d].append(v[d])
        return velocities
    
    def getFitness(self):
        return self._fit
    
    def getBestFitness(self):
        return self._pBestFit
# End class Particle;
