from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from tkinter import *


width, height = 500, 400
ox = -0.8
oy = -0.8
vx = 0.8
vy = 0.8

def draw_axes():
    glVertex2f(ox,oy)
    glVertex2f(vx,oy)                                   # bottom left point
    glVertex2f(ox,oy)
    glVertex2f(ox,vy)

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor(1.0, 1.0, 0.0)

    draw_axes()

    glEnd()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Projectile Simulator")
    glClearColor(1.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(draw)
    glutMainLoop()

main()
