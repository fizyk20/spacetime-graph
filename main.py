from PyQt4 import QtGui
from PyQt4.QtGui import QPainter, QColor
from PyQt4.QtOpenGL import QGLPixelBuffer
from OpenGL.GL import *
from math import sqrt
import sys

app = QtGui.QApplication(sys.argv)
width = 800
height = 600
aspect = width/height

buf = QGLPixelBuffer(width, height)

if not buf.makeCurrent():
    print('makeCurrent fail')
    
glMatrixMode(GL_PROJECTION)
glOrtho(-aspect, aspect, -1.0, 1.0, -1.0, 1.0)

glClearColor(0,0,0,1.0)
glClear(GL_COLOR_BUFFER_BIT)

glMatrixMode(GL_MODELVIEW)
glRotate(30, 0, 0, 1)

glBegin(GL_TRIANGLES)
glColor(1.0, 1.0, 1.0)
glVertex(-0.5, -sqrt(3)/6, 0.0)
glVertex(0.0, sqrt(3)/3, 0.0)
glVertex(0.5, -sqrt(3)/6, 0.0)
glEnd()

glFlush()

p = QPainter(buf)
p.setPen(QColor(0,255,255))
p.drawText(10, 20, 'Test')
p.end()

if not buf.toImage().save('test.png', 'PNG'):
    print('Coś nie wyszło')

#sys.exit(app.exec_())