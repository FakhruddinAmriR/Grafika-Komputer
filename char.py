from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pos_x = 0
pos_y = 0


w,h = 2000, 2000


def badan():
    global pos_x, pos_y
    glScale(0.3 , 0.3 , 0)
    glTranslated (pos_x, pos_y, 0)
    glTranslated(0, -500, 0)
    # pos_x-=0.5
    # if pos_x <= -1000:
    #     pos_x=0
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






# def tangan():

#     glBegin(GL_POLYGON)
#     glColor3ub(0, 0, 255)
#     glVertex2f(700, 400)
#     glVertex2f(900, 400)

#     glVertex2f(900, 400)
#     glVertex2f(900, 300)

#     glVertex2f(900, 300)
#     glVertex2f(600, 300)

#     glVertex2f(600, 300)
#     glVertex2f(600, 500)

#     glVertex2f(600, 500)
#     glVertex2f(700, 500)

#     glVertex2f(700, 500)
#     glVertex2f(700, 400)  
#     glEnd()

# def capit():

#     glColor3ub(80, 80, 80)
#     glBegin(GL_POLYGON)

    
def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1000, 1000, -1000, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def input_keyboard(key,x,y):
    global pos_x, pos_y

    if key == GLUT_KEY_UP:
        pos_y += 5
        print("Tombol Atas ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_DOWN:
        pos_y -= 5
        print("Tombol Bawah ditekan ", "x : ", pos_x, " y : ", pos_y)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    # kaki()
    badan()
    # mata()
    # tangan()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(input_keyboard)

glutMainLoop()





#mulai
def tombolmulai():
    glTranslated(250, 100, 0)
    glLineWidth(10)
    glColor3ub(85, 150, 20)
    glBegin(GL_LINE_LOOP)
    glVertex2f(50, 50)
    glVertex2f(50, 380)
    glVertex2f(100, 420)
    glVertex2f(240, 420)
    glVertex2f(300, 350)
    glVertex2f(300, 270)
    glVertex2f(250, 200)
    glVertex2f(200, 200)
    glVertex2f(160, 200)
    glVertex2f(200, 140)
    glVertex2f(240, 100)
    glVertex2f(300, 50)
    glVertex2f(200, 50)
    glVertex2f(140, 100)
    glVertex2f(100, 160)
    glVertex2f(100, 50)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2f(340, 280)
    glVertex2f(340, 400)
    glVertex2f(360, 420)
    glVertex2f(420, 420)
    glVertex2f(440, 400)
    glVertex2f(440, 280)
    glVertex2f(420, 260)
    glVertex2f(360, 260)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2f(460, 400)
    glVertex2f(480, 420)
    glVertex2f(520, 420)
    glVertex2f(540, 400)
    glVertex2f(540, 360)
    glVertex2f(520, 340)
    glVertex2f(540, 320)
    glVertex2f(540, 280)
    glVertex2f(520, 260)
    glVertex2f(480, 260)
    glVertex2f(460, 280)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2f(580, 400)
    glVertex2f(600, 420)
    glVertex2f(660, 420)
    glVertex2f(680, 400)
    glVertex2f(680, 280)
    glVertex2f(660, 260)
    glVertex2f(600, 260)
    glVertex2f(580, 280)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2f(360, 60)
    glVertex2f(340, 80)
    glVertex2f(340, 180)
    glVertex2f(360, 160)
    glVertex2f(360, 80)
    glVertex2f(400, 70)
    glVertex2f(440, 80)
    glVertex2f(440, 160)
    glVertex2f(460, 180)
    glVertex2f(460, 80)
    glVertex2f(440, 60)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2f(480, 180)
    glVertex2f(500, 180)
    glVertex2f(560, 80)
    glVertex2f(560, 180)
    glVertex2f(580, 180)
    glVertex2f(580, 60)
    glVertex2f(560, 60)
    glVertex2f(500, 140)
    glVertex2f(500, 60)
    glVertex2f(480, 60)
    glEnd()




    glPushMatrix()
    # glScale(0.2 , 0.2 , 0)
    glTranslated(charx, chary, 0)
    glColor3ub(255, 255, 255)

    glBegin(GL_POLYGON)
    glVertex2f(100, 140)
    glVertex2f(60, 140)
    glVertex2f(60, 240)
    glVertex2f(80, 260)
    glVertex2f(140, 260)
    glVertex2f(160, 240)
    glVertex2f(160, 140)
    glVertex2f(120, 140)
    glVertex2f(120, 120)
    glVertex2f(100, 120)
    glVertex2f(100, 140)
    glEnd() 

    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(160, 230)
    glVertex2f(140, 230)
    glVertex2f(130, 220)
    glVertex2f(140, 210)
    glVertex2f(160, 210)
    glEnd()
    
    
    glColor3ub(80, 80, 80) #hitam
    glBegin(GL_POLYGON)
    glVertex2f(60, 100)
    glVertex2f(60, 120)
    glVertex2f(160, 120)
    glVertex2f(160, 100)
    glEnd()
    glPopMatrix()