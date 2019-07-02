import turtle                                           # Import turtle library to use windows and graphical interface.
import math                                             # Import math to make some calculations below.

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

while Xo<1250:                      # X will be lower than window size.
    Tucus = (2 * Vy) / g                # Calculation of time of flying.
    t = 0                               # Resetting time value.
    while t<=Tucus:                     # Time shoul be lower than total time of flying.
        x = Xo + Vx*t                       # Calculation of "x" which is going to be used below to move turtle. ( circle ) 
        y = (Vy*t) - ((g*t**2)/2)           # Calculation of "y" which is going to be used below to move turtle. ( circle ) 

        turtle.pendown()
        turtle.shape("circle")              # Giving "circle" shape to the turtle object.
        turtle.shapesize(1)                 # Setting object size.
        turtle.goto(x,y)                    # Moving object.

        t=t+0.5                             # Increasing time (t) value.
    Xo = Xo + Tucus*Vx                  # Setting new X.
    Vy = Vy*0.8                         # Setting new Y.

    # point1 = (50, 100)
    # point2 = (150, 200)


    # turtle.penup()
    # turtle.goto(point1)
    # turtle.pendown()
    # turtle.goto(point2)

    # turtle.hideturtle()


turtle.done()                       # Closing window.