from .generic import GenericObject
import numpy
import FTGL
from OpenGL.GL import *

class Text(GenericObject):
    
    def __init__(self, text='Test', font='comic.ttf', size=1.0, **kwargs):
        self.text = text
        self.font = FTGL.PolygonFont(font)
        self.font.FaceSize(24)
        self.scale = size/self.font.line_height
        super(Text, self).__init__(**kwargs)
        
    def transform(self, m):
        m2 = numpy.identity(4, 'f')
        m2[0, 0] = m2[1, 1] = 0.0
        m2[1, 0] = m2[0, 1] = 1.0
        self._transform = numpy.dot(self._transform, m2)
        self._transform = numpy.dot(self._transform, m)
        self._transform = numpy.dot(self._transform, m2)
        
    def _draw(self):
        glScale(self.scale, self.scale, self.scale)
        self.font.Render(self.text)