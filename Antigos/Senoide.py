import turtle
import math
 
wn = turtle.Screen()
wn.bgcolor('lightgray')
toba = turtle.Turtle()
toba.shape('turtle')
toba.penup()
toba.backward(180)
toba.pendown()
for x in range(360):
	y = math.sin(math.radians(90))
	toba.left(y)
	toba.forward(x)
