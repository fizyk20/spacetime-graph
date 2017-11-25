from .generic import GenericObject
from OpenGL.GL import *
from math import cosh, sinh

class Hyperbola(GenericObject):
    
    def __init__(self, a=1, tmin=-4.0, tmax=4.0, steps=100, **kwargs):
        super(Hyperbola, self).__init__(**kwargs)
        self.a = a  #y = a*cosh(t), x = a*sinh(t)
        self.tmin = tmin
        self.tmax = tmax
        self.steps = steps
    
    def _draw(self):
        glBegin(GL_LINE_STRIP)
        t = self.tmin
        step = (self.tmax-self.tmin) / self.steps
        while t <= self.tmax:
            glVertex(self.a*sinh(t), self.a*cosh(t), 0.0)
            t += step
        glEnd()
    
