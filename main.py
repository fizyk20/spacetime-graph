from PyQt4 import QtGui
from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QPainter, QColor
from PyQt4.QtOpenGL import QGLPixelBuffer, QGLWidget
from OpenGL.GL import *
from math import sqrt
from lorentz import *
import sys
from objects import *
from datetime import datetime

app = QtGui.QApplication(sys.argv)
width = 800
height = 600
aspect = width/height

#buf = QGLPixelBuffer(width, height)

#if not buf.makeCurrent():
#    print('makeCurrent fail')
    
#glMatrixMode(GL_PROJECTION)
#glOrtho(-aspect, aspect, -1.0, 1.0, -1.0, 1.0)

s = Scene()
s.addObject(Hyperbola(0.2, color=(0.0, 1.0, 1.0)))
s.addObject(Hyperbola(0.53, color=(0.0, 1.0, 1.0)))
h = Hyperbola(0.2, color=(0.0, 1.0, 1.0))
h.rotate(90)
s.addObject(h)
h = Hyperbola(0.53, color=(0.0, 1.0, 1.0))
h.rotate(90)
s.addObject(h)
s.addObject(Line(p1=(-5,-5), p2=(5,5), color=(0.7, 0.7, 0.0)))
s.addObject(Line(p1=(5,-5), p2=(-5,5), color=(0.7, 0.7, 0.0)))

ziemia = Line(p1=(-4, 0.0), p2=(4, 0.0), color=(0, 0, 0))
s.addObject(ziemia)

s.addObject(Line(p1=(0.0, -4), p2=(0.0, 4), color=(0, 0, 0))) #Ziemia x

ziemia_t = Text(text='Ziemia', color=(0, 0, 0), size=0.1)
ziemia_t.translate(0.01, 0.3)
ziemia_t.rotate(90)
s.addObject(ziemia_t)

rakieta = Line(p1=(-4, -3), p2=(4, 3), color=(0, 0, 1))
s.addObject(rakieta)

s.addObject(Line(p1=(-3, -4), p2=(3, 4), color=(0, 0, 1))) #rakieta x

rakieta_t = Text(text='Rakieta', color=(0, 0, 1), size=0.1)
rakieta_t.translate(0.01, 0.6)
rakieta_t.rotate(54.3)
s.addObject(rakieta_t)

zyczenia1 = Line(p1=(0.2,0), p2=(0.8,0.6), color=(1, 0, 0))
s.addObject(zyczenia1)

zyczenia2 = Line(p1=(0.2,0), p2=(0.8,-0.6), color=(1, 0, 0))
zyczenia2.lorentz(0.75)
s.addObject(zyczenia2)


class Test(QGLWidget):
    
    def initializeGL(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-aspect, aspect, -1.0, 1.0, -1.0, 1.0)
        glViewport(0, 0, width, height)
    
    def paintGL(self):
        dt = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
        k = dt%10
        v = -(10-k)*0.75/5 if k > 5 else -k*0.75/5
        s.identity()
        s.lorentz(v)
        s.draw()
        QTimer.singleShot(1, self.updateGL)
        
    def resizeGL(self, w, h):
        width = w
        height = h
        aspect = width/height
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-aspect, aspect, -1.0, 1.0, -1.0, 1.0)

#if not buf.toImage().save('test.png', 'PNG'):
#    print('Coś nie wyszło')
    
w = Test()
w.resize(800, 600)
w.makeCurrent()
w.show()
w.updateGL()

sys.exit(app.exec_())