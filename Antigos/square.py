Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> wn = turtle.Screen()
>>> alex = turtle.Turtle()
>>> 
>>> for aColor in ["yellow","red","purple","blue"]:
	alex.color(aColor)
	alex.forward(50)
	alex.left(90)

	
>>> wn.exitonclick()
