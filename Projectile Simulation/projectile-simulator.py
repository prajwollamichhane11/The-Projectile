import turtle
from turtle import *
import math
import pygame
from time import time
from tkinter import *


PI = 3.14159265
g = 9.8

V = int(input("Enter the Initial Velocity: "))                                                 
aci = int(input("Enter the angle of inclination: "))

# Component of Initial Velocity on X-axis
Vx = V*math.cos(math.radians(aci))
# Component of Initial Velocity on Y-axis
Vy = V*math.sin(math.radians(aci))

# Creating Background for Project
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Horizontal Projectile Simulation")

# Initial point of the projectile
# Point of Intersection of the axes
Xo = 0
Yo = 0

# Counting the maximum height for first projectile
count = 0

# Setting the Window Sizes
turtle.setup(width=1250,height=600)

# Setting the Coordinates the object will start from and be displayed on the screen
turtle.setworldcoordinates(0, 0, 1250, 600)

# Finding the range for the first Projectile
horrange = (V**2*math.sin(2*(math.radians(aci))))/9.8
print("Range of First Projectile = " + str(horrange))

# Finding the maximum height height of the first projectile
maxheight = (V**2 * ((math.sin(math.radians(aci)))**2))/(2*9.8)
print("Max Height of First Projectile = " + str(maxheight))


#Background Music during the Projectile Motion
pygame.mixer.init()
pygame.mixer.music.load("onair.mp3")
pygame.mixer.music.play()


#Drawing the Axes
# X-axis
turtle.setpos(0,0)
turtle.shapesize(2)
turtle.left(0)
turtle.pendown()
turtle.forward(1250)
turtle.penup()
turtle.left(180)

# Y-axis
turtle.setpos(0,0)
turtle.right(90)
turtle.pendown()
turtle.forward(600)
turtle.penup()
turtle.left(180)
turtle.goto(0,0)
turtle.penup()


while Xo<1250:
    # Calculation of Time of Flight
    Tucus = (2 * Vy) / g
    t = 0
    start = time()
    while t<=Tucus:
        # Calculation of "x" to move turtle. ( circle )
        x = Xo + Vx*t 
        # Calculation of "y" to move turtle. ( circle ) 
        y = (Vy*t) - ((g*t**2)/2)

        # Gives shape of circle to turtle
        color('red')
        turtle.shape("circle")
        turtle.shapesize(1)
        turtle.pendown()
        turtle.goto(x,y)
        color('green')
        # Determines the Speed of movement of the turtle
        t=t+0.5

        if int(y) == int(maxheight) and count == 0:
            xMaxheight = x

            # Drawing Line from Maximun Height
            turtle.setpos(xMaxheight,maxheight)
            turtle.left(180)
            turtle.pendown()
            turtle.goto(xMaxheight,0)
            turtle.penup()
            turtle.goto(xMaxheight,maxheight)
            turtle.penup()
            count += 1


        # Dropping Sound Effect
        if y == 0 and x != 0:
            if timeDiff > 0.20:
                pygame.mixer.init()
                pygame.mixer.music.load("drop.wav")
                pygame.mixer.music.play()
                pygame.time.wait(100)

            
    end = time()
    timeDiff = end - start

    # Setting new X
    Xo = Xo + Tucus*Vx
    # Setting new Y
    Vy = Vy*0.8

    if timeDiff < 0.1:
        break

# turtle.setpos(0,0)
# turtle.forward(1250)
# turtle.hideturtle()

top = Tk()
top.title("Velocity/ACI")
top.geometry("500x200+500+700")


label1 =Label(top, text ="Horizontal Range for first Projectile   :")
label1.grid(row =0, column =0)
answer_label =Label(top, text ="---")
answer_label.grid(row =0, column =10)
answer_label.configure(text =horrange)


label2 =Label(top, text ="Maximum Height of first Projectile      :")
label2.grid(row =3, column =0)
answer1_label =Label(top, text ="---")
answer1_label.grid(row =3, column =10)
answer1_label.configure(text =maxheight)

# Closing the Window
turtle.done()