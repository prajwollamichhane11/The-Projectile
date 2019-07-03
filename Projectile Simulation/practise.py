# Python program to user input pattern 
# using Turtle Programming 
import turtle #Outside_In 
import math

turtle.position()
turtle.forward(50)
turtle.position()
turtle.hideturtle()


point1 = (50, 100)
point2 = (150, 200)


turtle.penup()
turtle.goto(point1)
turtle.pendown()
turtle.goto(point2)
turtle.penup()

turtle.hideturtle()
turtle.done()