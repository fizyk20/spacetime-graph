from .generic import GenericObject
from OpenGL.GL import *
from math import sqrt
import numpy
from numpy import linalg

class Arrow(GenericObject):
    
    def __init__(self, point=(0,0), dir=(1,0), **kwargs):
        super(Arrow, self).__init__(**kwargs)
        self.point = numpy.array(point, 'f')
        self.dir = numpy.array(dir, 'f')
        
    def _draw(self, **kwargs):
        p1 = self.point
        p2 = self.point + self.dir
        
        glBegin(GL_LINES)
        glColor(*self._color)
        glVertex(p1[1], p1[0], 0.0)
        glVertex(p2[1], p2[0], 0.0)
        glEnd()
        
        r = numpy.array((-self.dir[1], self.dir[0]), 'f')
        r /= linalg.norm(r)
        r *= linalg.norm(self.dir)*0.025
        p3 = p2 - 0.05*self.dir + r
        p4 = p2 - 0.05*self.dir - r
        glBegin(GL_TRIANGLES)
        glVertex(p2[1], p2[0], 0.0)
        glVertex(p3[1], p3[0], 0.0)
        glVertex(p4[1], p4[0], 0.0)
        glEnd()