from .generic import GenericObject
from OpenGL.GL import *
import numpy

class DottedLine(GenericObject):
    
    def __init__(self, p1=(0,0), p2=(0,0), dot_space=0.015, **kwargs):
        super(DottedLine, self).__init__(**kwargs)
        
        if not isinstance(p1, tuple) or len(p1) != 2:
            raise Exception
        
        if not isinstance(p2, tuple) or len(p2) != 2:
            raise Exception
        
        self.p1 = numpy.array(p1, 'f')
        self.p2 = numpy.array(p2, 'f')
        self.dot_space = dot_space
        
    def _draw(self, **kwargs):
        start = numpy.array(self.p1)
        end = numpy.array(self.p2)
        length = numpy.linalg.norm(end - start)
        num_steps = length/self.dot_space
        step = (end - start)/num_steps
        current = start
        while numpy.dot(end - current, step) >= 0:
            glBegin(GL_POINTS)
            glVertex(current[1], current[0], 0.0)
            glEnd()
            current += step
