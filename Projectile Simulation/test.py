import turtle                                           # Import turtle library to use windows and graphical interface.
import math

PI = 3.14159265                                         # Setting PI as variable.
V = int(input("Enter the Initial Velocity: "))                                                  # Setting first speed.
aci = int(input("Enter the angle of inclination: "))                                                # Setting angle of throwing.
g = 10                                                  # Setting gravitational acceleration.

Vx = V*math.cos(math.radians(aci))                      # Setting Vx speed
Vy = V*math.sin(math.radians(aci))                      # Setting Vy speed

Xo = 0                                          # Settin first X.
Yo = 0                                          # Settin first Y.

turtle.setup(width=1250,height=600)             # Set sizes of window.
turtle.setworldcoordinates(0, 0, 1250, 600)     # Set coordinatese where will object start from.

range = (V**2*math.sin(2*(math.radians(aci))))/9.8
print("Range of First Projectile = " + str(range))

maxheight = (V**2 * ((math.sin(math.radians(aci)))**2))/(2*9.8)
print("Max Height of First Projectile = " + str(maxheight))

turtle.setpos(0,0)
turtle.left(0)
turtle.pendown()
turtle.forward(1250)
turtle.penup()

turtle.setpos(0,0)
turtle.left(90)
turtle.pendown()
turtle.forward(600)
turtle.penup()

while Xo<1250:                      # X will be lower than window size.
    Tucus = (2 * Vy) / g                # Calculation of time of flying.
    t = 0                               # Resetting time value.
    while t<=Tucus:                     # Time shoul be lower than total time of flying.
        x = Xo + Vx*t                       # Calculation of "x" which is going to be used below to move turtle. ( circle ) 
        y = (Vy*t) - ((g*t**2)/2)           # Calculation of "y" which is going to be used below to move turtle. ( circle ) 

        turtle.penup()
        turtle.shape("circle")              # Giving "circle" shape to the turtle object.
        turtle.shapesize(1)                 # Setting object size.
        turtle.pendown()
        turtle.goto(x,y)                    # Moving object.

        t=t+0.5                             # Increasing time (t) value.


    Xo = Xo + Tucus*Vx                  # Setting new X.
    Vy = Vy*0.8                         # Setting new Y.

# turtle.setpos(0,0)
# turtle.forward(1250)
# turtle.hideturtle()

turtle.done()                       # Closing window.