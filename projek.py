from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


pos_x = 0
pos_y = 0

mulai = False
charx = 0
chary = 0
grafiti = 15
speed = 2
score = 0
perintah = True

def pohon():

    #daun
    glPushMatrix()
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
    glPopMatrix()

def char():
    global charx, chary, pos_x, pos_y
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

def jalan():

    global pos_x, pos_y, speed
    glPushMatrix()
    glTranslated(pos_x, pos_y, 0)

    print("pos_x =",pos_x)
    pos_x -= speed

    if pos_x <= -1500:
        pos_x = 0

    # glScale(10, 10, 0)
    glTranslated(0, 1, 0)
    glColor3ub(136, 69, 19)
    glBegin(GL_POLYGON)
    glVertex2f(0, 100)
    glVertex2f(2800, 100)
    glVertex2f(2800, 0)
    glVertex2f(0, 0)
    glEnd()   

    #rintangan
    glTranslated(0, 1, 0)
    glColor3ub(80, 80, 80)
    glBegin(GL_POLYGON)
    glVertex2f(1280, 100)
    glVertex2f(1280, 200)
    glVertex2f(1380, 200)
    glVertex2f(1380, 100)
    glEnd()
    glPopMatrix()
    

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

onfloor = True

def lompat(value = 0):
    global chary, onfloor, grafiti

    if onfloor==True:
        chary+=15
        glutTimerFunc(15,lompat,0)
        if chary >= 400:
            onfloor=False
    if onfloor==False and chary>=10:
        chary-=15
        glutTimerFunc(15,lompat,0)
    
def start(key,x,y):
    global mulai, chary, onfloor, gameover, menu
    
    if mulai == False:
        if key == b'\r':
            mulai = True
            menu = False
    
        if key == b' ':
            glutDestroyWindow(wind)

    if mulai == True and gameover == False:
        if key == b' ':
            onfloor = True
            lompat()

    if gameover == True:
        if key == b'\r':
            gameover = False
        
        if key == b' ':
            glutDestroyWindow(wind)

      
def collision():
    global charx, chary, pos_x, pos_y, mulai, gameover, perintah, menu
    if chary in range(pos_y+0, pos_y+100) and charx in range (int(pos_x)+1280, int(pos_x)+1380):
        print("kenaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        # mulai = False
        gameover = True
        pos_x = 0

    

def showscore():
    text = f'SCORE : {score}'
    glPushMatrix()
    glColor3ub(250, 0, 0)
    glRasterPos2f(20, 670)
    for i in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glPopMatrix()

def title_menu():
    global perintah
    text = f'TEKAN ENTER UNTUK MEMULAI'
    glPushMatrix()
    glColor3ub(80, 80, 80)
    glRasterPos2f(200, 10)
    if perintah == True:
        for i in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glPopMatrix()


def iterate():
    glViewport(0, 0, 1280, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 1280, 0, 700)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def gover():
    glTranslated(150, 100, 0)
    glColor3ub(250, 0, 0)
    glLineWidth(10)
    glBegin(GL_LINE_LOOP)
    glVertex2f(60, 300)
    glVertex2f(140, 500)
    glVertex2f(200, 500)
    glVertex2f(280, 480)
    glVertex2f(160, 480)
    glVertex2f(100, 320)
    glVertex2f(180, 320)
    glVertex2f(240, 380)
    glVertex2f(160, 380)
    glVertex2f(180, 400)
    glVertex2f(300, 400)
    glVertex2f(200, 300)
    glEnd()

    glColor3ub(250, 0, 0)
    glLineWidth(10)
    glBegin(GL_LINE_LOOP)
    glVertex2f(280, 300)
    glVertex2f(360, 500)
    glVertex2f(500, 500)
    glVertex2f(460, 300)
    glVertex2f(420, 300)
    glVertex2f(440, 380)
    glVertex2f(340, 380)
    glVertex2f(320, 300)
    glEnd()

    glColor3ub(250, 0, 0)
    glLineWidth(10)
    glBegin(GL_LINE_LOOP)
    glVertex2f(360, 420)
    glVertex2f(400, 470)
    glVertex2f(480, 470)
    glVertex2f(440, 420)
    glEnd()

    glColor3ub(250, 0, 0)
    glLineWidth(10)
    glBegin(GL_LINE_LOOP)
    glVertex2f(560, 500)
    glVertex2f(600, 500)
    glVertex2f(620, 420)
    glVertex2f(700, 500)
    glVertex2f(740, 500)
    glVertex2f(700, 300)
    glVertex2f(660, 300)
    glVertex2f(680, 400)
    glVertex2f(620, 340)
    glVertex2f(580, 420)
    glVertex2f(540, 300)
    glVertex2f(500, 300)
    glEnd()

    glColor3ub(250, 0, 0)
    glLineWidth(10)
    glBegin(GL_LINE_LOOP)
    glVertex2f(800, 500)
    glVertex2f(940, 500)
    glVertex2f(920, 480)
    glVertex2f(840, 480)
    glVertex2f(820, 420)
    glVertex2f(920, 420)
    glVertex2f(900, 380)
    glVertex2f(810, 380)
    glVertex2f(795, 320)
    glVertex2f(900, 320)
    glVertex2f(880, 300)
    glVertex2f(760, 300)
    glEnd()

    glColor3ub(250, 0, 0)
    glLineWidth(10)
    glBegin(GL_LINE_LOOP)
    glVertex2f(170, 220)
    glVertex2f(200, 260)
    glVertex2f(300, 260)
    glVertex2f(320, 220)
    glVertex2f(320, 80)
    glVertex2f(300, 50)
    glVertex2f(200, 50)
    glVertex2f(170, 80)
    glEnd()

    glColor3ub(250, 0, 0)
    glLineWidth(10)
    glBegin(GL_LINE_LOOP)
    glVertex2f(380, 260)
    glVertex2f(440, 80)
    glVertex2f(460, 80)
    glVertex2f(520, 260)
    glVertex2f(540, 260)
    glVertex2f(480, 60)
    glVertex2f(420, 60)
    glVertex2f(360, 260)
    glEnd()

    glColor3ub(250, 0, 0)
    glLineWidth(10)
    glBegin(GL_LINE_LOOP)
    glVertex2f(700, 250)
    glVertex2f(700, 220)
    glVertex2f(600, 220)
    glVertex2f(600, 160)
    glVertex2f(700, 160)
    glVertex2f(700, 140)
    glVertex2f(600, 140)
    glVertex2f(600, 80)
    glVertex2f(700, 80)
    glVertex2f(700, 50)
    glVertex2f(570, 50)
    glVertex2f(570, 250)
    glEnd()

    glColor3ub(250, 0, 0)
    glLineWidth(10)
    glBegin(GL_LINE_LOOP)
    glVertex2f(730, 250)
    glVertex2f(820, 250)
    glVertex2f(860, 220)
    glVertex2f(860, 160)
    glVertex2f(840, 140)
    glVertex2f(780, 140)
    glVertex2f(860, 60)
    glVertex2f(820, 40)
    glVertex2f(760, 140)
    glVertex2f(760, 70)
    glVertex2f(720, 70)
    glEnd()

gameover = False
def showScreen():
    global mulai, speed, score
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glutSwapBuffers()
    glClearColor(0, 200, 200, 1)
    # if chary >= 480:
    #     chary -= grafiti
  
    if mulai == True and gameover == False: 
        if pos_x == 0:
            score += 1
        if pos_x == 0:
            speed+=0.2
        pohon()
        char()
        jalan()
        collision()
        showscore()
    elif mulai == True and gameover == True:
        score = -1
        speed = 2
        gover()
        title_menu()
    
    elif mulai == False:
        score = -1
        speed = 2
        tombolmulai()
        title_menu()

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