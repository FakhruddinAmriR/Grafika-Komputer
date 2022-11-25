from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h = 2000, 2000

    
def kaki():
    
    glTranslated(0, -500, 0)
    glColor3ub(80, 80, 80) #hitam
    glBegin(GL_POLYGON)
    glVertex2f(400, 40)
    glVertex2f(300, 40)

    glVertex2f(300, 40)
    glVertex2f(300, 140)

    glVertex2f(300, 140)
    glVertex2f(600, 140)

    glVertex2f(600, 140)
    glVertex2f(600, 100)

    glVertex2f(600, 100)
    glVertex2f(500, 100)

    glVertex2f(400, 00)
    glVertex2f(700, 00)

    glVertex2f(700, 100)
    glVertex2f(400, 100)

    glEnd()


def badan():

    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(500, 200)
    glVertex2f(300, 200)
    
    #bentuk1
    glVertex2f(300, 200)
    glVertex2f(300, 700)

    glVertex2f(300, 700)
    glVertex2f(400, 800)

    glVertex2f(400, 800)
    glVertex2f(700, 800)
    
    #bentuk2
    # glVertex2f(300, 200)
    # glVertex2f(300, 800)

    # glVertex2f(300, 800)
    # glVertex2f(700, 800)

    glVertex2f(700, 800)
    glVertex2f(800, 700)

    glVertex2f(800, 700)
    glVertex2f(800, 200)

    glVertex2f(800, 200)
    glVertex2f(600, 300)

    glVertex2f(600, 300)
    glVertex2f(600, 100)

    glVertex2f(600, 100)
    glVertex2f(500, 100)

    glVertex2f(500, 100)
    glVertex2f(500, 300)
    glEnd()

def mata():
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(800, 700)
    glVertex2f(640, 700)

    glVertex2f(640, 700)
    glVertex2f(600, 640)

    glVertex2f(600, 640)
    glVertex2f(640, 580)

    glVertex2f(640, 580)
    glVertex2f(800, 580)
    glEnd()

def tangan():

    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 255)
    glVertex2f(700, 400)
    glVertex2f(900, 400)

    glVertex2f(900, 400)
    glVertex2f(900, 300)

    glVertex2f(900, 300)
    glVertex2f(600, 300)

    glVertex2f(600, 300)
    glVertex2f(600, 500)

    glVertex2f(600, 500)
    glVertex2f(700, 500)

    glVertex2f(700, 500)
    glVertex2f(700, 400)  
    glEnd()

def capit():

    glColor3ub(80, 80, 80)
    glBegin(GL_POLYGON)

    
def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1000, 1000, -1000, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    kaki()
    badan()
    mata()
    tangan()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()