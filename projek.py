from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pos_x = 0
pos_y = 0

mulai = False

def pohon():

    #daun
    glColor3ub(0, 250, 0)
    glTranslate(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(150, 140)
    glVertex2f(100, 140)
    glVertex2f(175, 300)
    glVertex2f(250, 140)
    glVertex2f(200, 140)
    glEnd()

    #batang
    glColor3ub(139, 69, 19)
    glBegin(GL_POLYGON)
    glVertex2f(200, 100)
    glVertex2f(150, 100)
    glVertex2f(150, 140)
    glVertex2f(200, 140)
    glEnd()

    #daun2
    glColor3ub(10, 200, 10) #putih
    glBegin(GL_POLYGON)
    glVertex2f(270, 180)
    glVertex2f(220, 180)
    glVertex2f(300, 450)
    glVertex2f(370, 180)
    glVertex2f(320, 180)
    glEnd()

    #daun3
    glColor3ub(160, 82, 45)
    glBegin(GL_POLYGON)
    glVertex2f(320, 100)
    glVertex2f(320, 180)
    glVertex2f(270, 180)
    glVertex2f(270, 100)
    glEnd()

def char():

    glScale(0.2 , 0.2 , 0)
    glTranslated(0, 480, 0)
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(500, 200)
    glVertex2f(300, 200)

    glVertex2f(300, 200)
    glVertex2f(300, 700)

    glVertex2f(300, 700)
    glVertex2f(400, 800)

    glVertex2f(400, 800)
    glVertex2f(700, 800)
      
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

def jalan():

    global pos_x, pos_y
    glTranslated(pos_x, pos_y, 0)

    pos_x-=5
    if pos_x <= -5000:
        pos_x = 0
    glScale(20, 20, 0)
    glTranslated(0, 1, 0)
    glColor3ub(136, 69, 19)
    glBegin(GL_POLYGON)
    glVertex2f(0, -100)
    glVertex2f(1000, -100)
    glVertex2f(1000, 00)
    glVertex2f(0, 00)
    glEnd()

    glTranslated(0, 1, 0)
    glColor3ub(80, 80, 80)
    glBegin(GL_POLYGON)
    glVertex2f(200, -1)
    glVertex2f(200, 20)
    glVertex2f(220, 20)
    glVertex2f(220, -1)
    glEnd()

def tombolmulai():
    glColor3ub(80, 80, 80)
    glBegin(GL_POLYGON)
    glVertex2f(200, 50)
    glVertex2f(200, 20)
    glVertex2f(220, 20)
    glVertex2f(220, 50)
    glEnd()

def start(key,x,y):
    global mulai
    if key == b'\r':
        mulai = True


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
    if mulai == True:
        
        pohon()
        char()
        jalan()
    else :
        tombolmulai()
    glFlush()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1280, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutKeyboardFunc(start)
glutMainLoop()