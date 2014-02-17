from .generic import GenericObject
from OpenGL.GL import *
from math import sqrt
import numpy
from numpy import linalg

class Line(GenericObject):
    
    def __init__(self, point=(0,0), dir=(1,0), **kwargs):
        super(Line, self).__init__(**kwargs)
        
        if not isinstance(point, tuple) or len(point) != 2:
            raise Exception
        
        if not isinstance(dir, tuple) or len(dir) != 2:
            raise Exception
        
        self.point = numpy.array(point, 'f')
        self.dir = numpy.array(dir, 'f')
        if linalg.norm(dir) == 0:
            raise Exception
        self.dir /= linalg.norm(dir)
        
    def _draw(self, **kwargs):
        p1 = numpy.array(kwargs.get('p1', (-1, -1)), 'f')
        p2 = numpy.array(kwargs.get('p2', (1, 1)), 'f')
        pl = [p1, p2]
        t1 = 0
        t2 = 0
        for i in range(8):
            p = numpy.array([0, 0, 0], 'f')
            p[0] = pl[(i & 4) >> 2][0]
            p[1] = pl[(i & 2) >> 1][1]
            t = numpy.dot(p - self.point, self.dir)
            if t < t1: t1 = t
            if t > t2: t2 = t
        p1 = self.point + t1*self.dir
        p2 = self.point + t2*self.dir
        glBegin(GL_LINES)
        glColor(*self._color)
        glVertex(p1[1], p1[0], 0.0)
        glVertex(p2[1], p2[0], 0.0)
        glEnd()