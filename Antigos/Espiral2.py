import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')

cTurtle = turtle.Turtle()
 
def espiral(comp_min, comp_max, passo, angulo):
    """Desenho de espirais por justaposição de segmentos de recta que
vão rodando de um certo ângulo. Assumo sentido crescente e rotação
idêntica à dos ponteiros do rrelógio."""
    cTurtle.down()
    for segmento in range(comp_min, comp_max, passo):
        cTurtle.forward(segmento)
        cTurtle.right(angulo)
        cTurtle.hideturtle()


espiral(10,200,3,90)
