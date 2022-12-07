from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def gameover():
    glBegin(GL_POLYGON)
    glVertex2f



def iterate():
    glViewport(0, 0, 1280, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 1280, 0, 700)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global mulai
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glutSwapBuffers()
    glClearColor(0, 200, 200, 1)


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()