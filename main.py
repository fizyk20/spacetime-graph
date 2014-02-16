from PyQt4 import QtGui
from PyQt4.QtOpenGL import QGLPixelBuffer
from OpenGL.GL import *
import sys

app = QtGui.QApplication(sys.argv)

print('Yo')
buf = QGLPixelBuffer(800,600)
print('Joł')

if not buf.makeCurrent():
    print('makeCurrent fail')

glClearColor(0,0,0,1.0)
glClear(GL_COLOR_BUFFER_BIT)

glBegin(GL_TRIANGLES)
glColor(1.0, 1.0, 1.0)
glVertex(-0.5, -0.2, 0.0)
glVertex(0.0, 0.8, 0.0)
glVertex(0.5, -0.2, 0.0)
glEnd()

glFlush()

if not buf.toImage().save('test.png', 'PNG'):
    print('Coś nie wyszło')

#sys.exit(app.exec_())