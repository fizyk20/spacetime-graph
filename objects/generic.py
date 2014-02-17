import numpy
from math import sin, cos, pi
from OpenGL.GL import *

class GenericObject:
    
    def __init__(self):
        self._color = (0, 0, 0)
        self._transform = numpy.identity(4)
        self._matrix_stack = []
        
    def draw(self, **kwargs):
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
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
        
    def translate(self, x=0, y=0, z=0):
        m = numpy.identity(4)
        m[0,3] = x
        m[1,3] = y
        m[2,3] = z
        self.transform(m)
        
    def rotate(self, angle, x=0, y=0, z=1):
        m = numpy.identity(4)
        angle *= pi/180
        c = cos(angle)
        s = sin(angle)
        m[0, 0] = x*x*(1-c) + c
        m[1, 1] = y*y*(1-c) + c
        m[2, 2] = z*z*(1-c) + c
        m[0, 1] = x*y*(1-c) - z*s
        m[0, 2] = x*z*(1-c) + y*s
        m[1, 0] = y*x*(1-c) + z*s
        m[1, 2] = y*z*(1-c) - x*s
        m[2, 0] = z*x*(1-c) - y*s
        m[2, 1] = z*y*(1-c) + x*s
        self.transform(m)
    