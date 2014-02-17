from .generic import GenericObject
from OpenGL.GL import *
from math import cosh, sinh

class Hyperbola(GenericObject):
    
    def __init__(self, a=1, **kwargs):
        super(Hyperbola, self).__init__(**kwargs)
        self.a = a  #y = a*cosh(t), x = a*sinh(t)
    
    def _draw(self, **kwargs):
        tmin = kwargs.get('tmin', -3.0)
        tmax = kwargs.get('tmax', 3.0)
        glBegin(GL_LINE_STRIP)
        t = tmin
        step = (tmax-tmin) / 100
        while t <= tmax:
            glVertex(self.a*sinh(t), self.a*cosh(t), 0.0)
            t += step
        glEnd()
    