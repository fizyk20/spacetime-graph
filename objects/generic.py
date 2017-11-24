import numpy
from math import sin, cos, pi, sqrt
from OpenGL.GL import *

class GenericObject:
    
    def __init__(self, **kwargs):
        self._color = kwargs.get('color', (0, 0, 0))
        self._transform = numpy.identity(4, 'f')
        self._matrix_stack = []
        
    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glMultMatrixf(self._transform)
        glColor(*self._color)
        self._draw()
        glPopMatrix()
        
    def _draw(self):
        raise NotImplementedError
    
    def setColor(self, r, g, b):
        self._color = (r, g, b)
        
    def identity(self):
        self._transform = numpy.identity(4, 'f')
        
    def transform(self, m):
        self._transform = numpy.dot(self._transform, m)
        
    def pushMatrix(self):
        self._matrix_stack.append(self._transform)
            
    def popMatrix(self):
        if len(self._matrix_stack) == 0:
            raise Exception
        self._transform = self._matrix_stack[-1]
        self._matrix_stack = self._matrix_stack[:-1]
        
    def translate(self, x=0, y=0):
        m = numpy.identity(4, 'f')
        m[3,0] = x
        m[3,1] = y
        self.transform(m)
        
    def rotate(self, angle):
        m = numpy.identity(4, 'f')
        c = cos(angle)
        s = sin(angle)
        m[0, 0] = c
        m[1, 1] = c
        m[0, 1] = -s
        m[1, 0] = s
        self.transform(m)
        
    def lorentz(self, v):
        m = numpy.identity(4, 'f')
        gamma = 1/sqrt(1-v*v)
        m[0, 0] = gamma
        m[1, 1] = gamma
        m[0, 1] = gamma*v
        m[1, 0] = gamma*v
        self.transform(m)
        
    
