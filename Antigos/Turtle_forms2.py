import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)


wn = turtle.Screen()
wheel = turtle.Turtle()

drawCircle(wheel,50)


def desenhaBarra(t, altura):
    """Faca a tartaruga t desenhar uma barra, de altura `altura`."""
    t.left(90)               # Apontar
    t.forward(altura)        # Desenha o lado esquerdo
    t.right(90)
    t.forward(40)            # largura da barra no topo
    t.right(90)
    t.forward(altura)        # e abaixo novamente!
    t.left(90)               # coloca a tartaruga na posição que a encontramos

...
for v in xs:                 # assuma que xs e tess estão prontas
    desenhaBarra(wheel, v)

wn.exitonclick()
