from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from tkinter import *
from math import sin, cos, radians, pi
import turtle 


width, height = 1000, 1000
ox = -0.8
oy = -0.8
vx = 0.8
vy = 0.8
clock = 0.00001
g = 9.8
arr_x = []
arr_y = []


def draw_axes():
    glVertex2f(vx,oy)
    glVertex2f(ox,oy)
    glVertex2f(ox,vy)

    print ("This program draws shapes based on the number you enter in a uniform pattern.") 
    num_str = input("Enter the side number of the shape you want to draw: ") 
    if num_str.isdigit(): 
        squares = int(num_str) 

    angle = 180 - 180*(squares-2)/squares 

    turtle.up()

    x = 0
    y = 0
    turtle.setpos(x, y) 


    numshapes = 8
    for x in range(numshapes): 
        turtle.color(random.random(), random.random(), random.random()) 
        x += 5
        y += 5
        turtle.forward(x) 
        turtle.left(y) 
        for i in range(squares): 
            turtle.begin_fill() 
            turtle.down() 
            turtle.forward(40) 
            turtle.left(angle) 
            turtle.forward(40) 
            print (turtle.pos()) 
            turtle.up() 
            turtle.end_fill() 

    time.sleep(11) 
    turtle.bye() 



def keyboard(key, x, y):
    if key == chr(27):
        sys.exit(0)

def draw():
    glLineWidth(5.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor(0.0, 1.0, 1.0)

    draw_axes()

    glEnd()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Projectile Simulator")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(draw)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

main()
