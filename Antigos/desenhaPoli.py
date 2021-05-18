import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')

tess = turtle.Turtle()
tess.color('purple')
tess.pensize(5)

def desenhaPoli(t,numLados,tamanho):
    
    for i in range(numLados):
        t.forward(tamanho)
        t.left((360 / numLados))
    

    
desenhaPoli(tess,40,61)
