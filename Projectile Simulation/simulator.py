from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from tkinter import *
from math import sin, cos, radians, pi


width, height = 500, 400
ox = -0.8
oy = -0.8
vx = 0.8
vy = 0.8
clock = 0.001
g = 9.8
arr_x = []
arr_y = []
t = 0

u = int(input("Enter the initial velocity: "))
theta = float(input("Enter the initial angle at which the projectile is thrown from the ground: "))
theta = radians(theta)
#Time of Flight
T = 2*u*sin(theta)//g

while t<= T:
    x = u * cos(theta) * t
    y = u * sin(theta) * t - 0.5*g*t**2
    print(x)
    print(y)
    arr_x.append(x+ox)
    arr_y.append(y+oy)

    t += clock

def draw_axes():
    glVertex2f(ox,oy)
    glVertex2f(vx,oy)
    glVertex2f(ox,oy)
    glVertex2f(ox,vy)

def draw_trajectory():
    for i in range(len(arr_x)):
        glVertex2f(arr_x[i],arr_y[i])


def draw():
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
    glutMainLoop()

main()
