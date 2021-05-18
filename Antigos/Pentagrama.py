import turtle
wn = turtle.Screen()
wn.bgcolor('orange')
tess = turtle.Turtle()
tess.shape('turtle')

 
def pentagrama(t,a,d):
    for angulo in range(5):
        t.left(a)
        t.forward(d)



for i in range(5):
    pentagrama(tess, -144,100)
    tess.penup()
    tess.forward(350)
    tess.left(-144)
    tess.pendown()
	
