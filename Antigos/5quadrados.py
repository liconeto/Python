import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of sz."""

    for i in range(40):
        t.forward(sz)
        t.left(90)
        t.forward(3)

wn = turtle.Screen()
wn.bgcolor('lightgray')

tess = turtle.Turtle()
tess.shape('turtle')

drawSquare(tess, 150)
