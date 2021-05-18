import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')

mosca = turtle.Turtle()
mosca.shape('turtle')

larg = turtle.Turtle()
larg.shape('turtle')
larg.color('red')
def desenhaQuadrado(t,tam):

    for i in range(4):
        t.forward(tam)
        t.left(90)


tamanho = 20

for i in range(10):
    desenhaQuadrado(mosca,tamanho)
    desenhaQuadrado(larg, (tamanho + 6))
    mosca.goto (-(tamanho / 2), -(tamanho / 2))
    larg.goto (-((tamanho + 6) / 2), -((tamanho + 6 )/ 2))
    tamanho = tamanho + 20
    
