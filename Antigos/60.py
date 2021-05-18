import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

fred = turtle.Turtle()


for angle in range(360):
    y = math.sin(math.radians(angle))
   
    fred.right(angle)
    fred.forward(angle)
    fred.left(-y)
    fred.forward(-y)
    
wn.exitonclick()
