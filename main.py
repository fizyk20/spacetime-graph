from PyQt4 import QtGui
from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QPainter, QColor
from PyQt4.QtOpenGL import QGLPixelBuffer, QGLWidget
from OpenGL.GL import *
import math
from math import sqrt
from lorentz import *
import sys
from objects import *
from datetime import datetime

def add_grid(s):
    a = -5
    while a <= 5:
        if a == 0.0:
            a += 0.125
        s.addObject(Line(p1=(-5,a), p2=(5,a), color=(0.8, 0.8, 1.0)))
        s.addObject(Line(p1=(a,-5), p2=(a,5), color=(0.8, 0.8, 1.0)))
        if a % 0.25 == 0:
            tick_t = Text(text='%.2f' % a, color=(0.0, 0.0, 0.2), size=0.07)
            tick_t.translate(a, 0.01)
            s.addObject(tick_t)
            tick_x = Text(text='%.2f' % a, color=(0.0, 0.0, 0.2), size=0.07)
            tick_x.rotate(-math.pi/4)
            tick_x.translate(-0.03, a)
            s.addObject(tick_x)
        a += 0.125

def add_hyperbolas(s):
    param = 0.25
    while param <= 1:
        for i in range(0,4):
            h = Hyperbola(param, color=(0.0, 1.0, 1.0))
            h.rotate(i*math.pi/2)
            s.addObject(h)
        param += 0.25

def add_circles(s):
    param = 0.25
    while param <= 1:
        s.addObject(Circle(param, color=(0.0, 1.0, 1.0)))
        param += 0.25

def add_labels(s):
    label_t = Text(text='t', color=(0.0, 0.0, 0.2), size=0.1)
    label_x = Text(text='x', color=(0.0, 0.0, 0.2), size=0.1)
    label_t.translate(0.82, 0.01)
    s.addObject(label_t)
    label_x.translate(0.01, 0.82)
    s.addObject(label_x)

def create_euclidean_scene():
    s = Scene()
    add_circles(s)
    # "light cone"
    s.addObject(Line(p1=(-5,-5), p2=(5,5), color=(0.7, 0.7, 0.0)))
    s.addObject(Line(p1=(5,-5), p2=(-5,5), color=(0.7, 0.7, 0.0)))
    # axes
    s.addObject(Line(p1=(-5,0), p2=(5,0), color=(0.0, 0.0, 0.2)))
    s.addObject(Line(p1=(0,-5), p2=(0,5), color=(0.0, 0.0, 0.2)))
    # grid
    add_grid(s)
    # axis labels
    add_labels(s)
    return s

def create_minkowski_scene():
    s = Scene()
    add_hyperbolas(s)
    # light cone
    s.addObject(Line(p1=(-5,-5), p2=(5,5), color=(0.7, 0.7, 0.0)))
    s.addObject(Line(p1=(5,-5), p2=(-5,5), color=(0.7, 0.7, 0.0)))
    # axes
    s.addObject(Line(p1=(-5,0), p2=(5,0), color=(0.0, 0.0, 0.2)))
    s.addObject(Line(p1=(0,-5), p2=(0,5), color=(0.0, 0.0, 0.2)))
    # grid
    add_grid(s)
    # axis labels
    add_labels(s)
    return s

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

def main():
    width = 600
    height = 450
    aspect = width/height
    app = QtGui.QApplication(sys.argv)
    buf = QGLPixelBuffer(width, height)

    if not buf.makeCurrent():
        print('makeCurrent fail')
    
    glMatrixMode(GL_PROJECTION)
    glOrtho(-aspect, aspect, -1.0, 1.0, -1.0, 1.0)

    m = create_minkowski_scene()
    e = create_euclidean_scene()

    for k in range(200):
        print(k, '...')
        param = math.sin(k/200*2*math.pi)*math.pi/2
        m.identity()
        m.lorentz(math.tanh(param))
        m.draw()
        buf.toImage().save('images/minkowski/%03d.png' % k, 'PNG')
        e.identity()
        e.rotate(param)
        e.draw()
        buf.toImage().save('images/euclidean/%03d.png' % k, 'PNG')

    buf.doneCurrent()
    
if __name__ == '__main__':
    main()
