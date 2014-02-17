import numpy
from math import sqrt

def lorentz2d(v):
    m = numpy.identity(4)
    gamma = 1/sqrt(1-v*v)
    m[0,0] = m[1,1] = gamma
    m[0,1] = m[1,0] = gamma*v
    return m