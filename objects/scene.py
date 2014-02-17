from .generic import GenericObject
from OpenGL.GL import *

class Scene(GenericObject):
    
    def __init__(self, clearColor = (1.0, 1.0, 1.0, 1.0), **kwargs):
        self._objects = []
        self.clearColor = clearColor
        super(Scene, self).__init__(**kwargs)
        
    def addObject(self, o):
        self._objects.append(o)
        
    def draw(self):
        glClearColor(*self.clearColor)
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        super(Scene, self).draw()
        glFlush()
        
    def _draw(self):
        for o in self._objects:
            o.draw()