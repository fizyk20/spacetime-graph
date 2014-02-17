import numpy
from math import sin, cos, pi
from OpenGL.GL import *

class GenericObject:
    
    def __init__(self, **kwargs):
        self._color = kwargs.get('color', (0, 0, 0))
        self._transform = numpy.identity(4, 'f')
        self._matrix_stack = []
        
    def draw(self, **kwargs):
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glMultMatrixd(self._transform)
        self._draw(**kwargs)
        glPopMatrix()
        
    def _draw(self, **kwargs):
        raise NotImplementedError
    
    def setColor(self, r, g, b):
        self._color = (r, g, b)
        
    def transform(self, m):
        self._transform *= m
        
    def pushMatrix(self):
        self._matrix_stack.append(self._transform)
            
    def popMatrix(self):
        if len(self._matrix_stack) == 0:
            raise Exception
        self._transform = self._matrix_stack[-1]
        self._matrix_stack = self._matrix_stack[:-1]
        
    def translate(self, x=0, y=0):
        m = numpy.identity(4, 'f')
        m[0,3] = x
        m[1,3] = y
        m[2,3] = 0
        self.transform(m)
        
    def rotate(self, angle):
        m = numpy.identity(4, 'f')
        angle *= pi/180
        c = cos(angle)
        s = sin(angle)
        m[0, 0] = c
        m[1, 1] = c
        m[0, 1] = -s
        m[1, 0] = s
        self.transform(m)
    