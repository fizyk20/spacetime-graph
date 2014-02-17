from .generic import GenericObject
from OpenGL.GL import *
from math import sqrt
import numpy
from numpy import linalg

class Line(GenericObject):
    
    def __init__(self, p1=(0,0), p2=(0,0), **kwargs):
        super(Line, self).__init__(**kwargs)
        
        if not isinstance(p1, tuple) or len(p1) != 2:
            raise Exception
        
        if not isinstance(p2, tuple) or len(p2) != 2:
            raise Exception
        
        self.p1 = numpy.array(p1, 'f')
        self.p2 = numpy.array(p2, 'f')
        
    def _draw(self, **kwargs):
        glBegin(GL_LINES)
        glVertex(self.p1[1], self.p1[0], 0.0)
        glVertex(self.p2[1], self.p2[0], 0.0)
        glEnd()