import turtle
import math

PI = 3.14159265
g = 9.8

V = int(input("Enter the Initial Velocity: "))                                                 
aci = int(input("Enter the angle of inclination: "))

# Component of Initial Velocity on X-axis
Vx = V*math.cos(math.radians(aci))
# Component of Initial Velocity on Y-axis
Vy = V*math.sin(math.radians(aci))


# Initial point of the projectile
# Point of Intersection of the axes
Xo = 0
Yo = 0

# Setting the Window Sizes
turtle.setup(width=1250,height=600)

# Setting the Coordinates the object will start from and be displayed on the screen
turtle.setworldcoordinates(0, 0, 1250, 600)

# Finding the range for the first Projectile
range = (V**2*math.sin(2*(math.radians(aci))))/9.8
print("Range of First Projectile = " + str(range))

# Finding the maximum height height of the first projectile
maxheight = (V**2 * ((math.sin(math.radians(aci)))**2))/(2*9.8)
print("Max Height of First Projectile = " + str(maxheight))


#Drawing the Axes
# X-axis
turtle.setpos(0,0)
turtle.left(0)
turtle.pendown()
turtle.forward(1250)
turtle.penup()

# Y-axis
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

        turtle.shape("circle")              # Giving "circle" shape to the turtle object.
        turtle.shapesize(1)                 # Setting object size.
        turtle.pendown()
        turtle.goto(x,y)                    # Moving object.

        t=t+0.5                             # Increasing time (t) value.

        if int(y) == int(maxheight):
            xMaxheight = x
            print(xMaxheight)
            # Drawing Line from Maximun Height
            turtle.setpos(xMaxheight,maxheight)
            turtle.left(180)
            turtle.pendown()
            turtle.forward(maxheight)
            turtle.penup()
    

    Xo = Xo + Tucus*Vx                  # Setting new X.
    Vy = Vy*0.8                         # Setting new Y.

# turtle.setpos(0,0)
# turtle.forward(1250)
# turtle.hideturtle()

turtle.done()                       # Closing window.