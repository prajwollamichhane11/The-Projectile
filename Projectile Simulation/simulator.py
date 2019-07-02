from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from tkinter import *
from math import sin, cos, radians, pi
import sys

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


def draw_trajectory():
    t = 0
    u = int(input("Enter the initial velocity: "))
    theta = float(input("Enter the initial angle at which the projectile is thrown from the ground: "))
    theta = radians(theta)

    #Time of Flight
    T = 2*u*sin(theta)/g

    while t <= T:
        x = u * cos(theta) * t
        y = u * sin(theta) * t - 0.5 * (g) * (t**2)
        print(x/100)
        print(y/100)
        glVertex2f(ox+(x/100),oy+(y/100))
        t += clock

def keyboard(key, x, y):
    if key == chr(27):
        sys.exit(0)

def draw():
    glLineWidth(5.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor(0.0, 1.0, 1.0)

    draw_axes()
    draw_trajectory()

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
