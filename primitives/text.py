from .generic import GenericObject
import numpy
import FTGL
from OpenGL.GL import *

def into_translation_rotation(m, axis_align):
    translation = numpy.identity(4, 'f')
    translation[3, 0] = m[3, 0]
    translation[3, 1] = m[3, 1]
    m[3, 0] = 0
    m[3, 1] = 0
    x = [translation[3, 0], translation[3, 1], 0, 1]
    x1 = [translation[3, 0], translation[3, 1], 0, 1]
    x1[axis_align] += 1
    Ax = numpy.dot(m, x)[0:2]
    Ax1 = numpy.dot(m, x1)[0:2]
    Rx = Ax1 - Ax
    x = [0, 0]
    x[axis_align] = 1
    norm_x = numpy.linalg.norm(x)
    norm_Rx = numpy.linalg.norm(Rx)
    cos_ang = numpy.dot(x, Rx) / norm_x / norm_Rx
    sin_ang = (x[0]*Rx[1] - x[1]*Rx[0]) / norm_x / norm_Rx
    rotation = numpy.identity(4, 'f')
    rotation[0, 0] = rotation[1, 1] = cos_ang
    rotation[0, 1] = -sin_ang
    rotation[1, 0] = sin_ang
    return translation, rotation

class Text(GenericObject):
    
    def __init__(self, text='Test', font='comic.ttf', size=1.0, axis_align=1, **kwargs):
        self.text = text
        self.font = FTGL.PolygonFont(font)
        self.font.FaceSize(24)
        self.scale = size/self.font.line_height
        self.axis_align = axis_align
        super(Text, self).__init__(**kwargs)
        
    def transform(self, m):
        m2 = numpy.identity(4, 'f')
        m2[0, 0] = m2[1, 1] = 0.0
        m2[1, 0] = m2[0, 1] = 1.0
        self._transform = numpy.dot(self._transform, m2)
        self._transform = numpy.dot(self._transform, m)
        self._transform = numpy.dot(self._transform, m2)
        
    def draw(self):
        # get the full transformation matrix for the text
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glMultMatrixf(self._transform)
        model = glGetDoublev(GL_MODELVIEW_MATRIX)
        glPopMatrix()
        # get the translation and rotation part
        t, r = into_translation_rotation(model, self.axis_align)
        # get the transformation without translation
        transform = self._transform.copy()
        transform[3, 0] = 0
        transform[3, 1] = 0
        # do the transformation
        glPushMatrix()
        glLoadIdentity()
        glMultMatrixf(t)
        glMultMatrixf(r)
        glColor(*self._color)
        self._draw()
        glPopMatrix()
        
    def _draw(self):
        glScale(self.scale, self.scale, self.scale)
        self.font.Render(self.text)
