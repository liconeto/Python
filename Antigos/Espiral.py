import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')

mosca = turtle.Turtle()
mosca.shape('turtle')
mosca.color('blue')

def desenhaQuadrado(t,tam):

    for i in range(4):
        
        t.forward(tam)
        t.left(90)
        

for i in range(25):
    tamanho = 5   
    desenhaQuadrado(mosca,tamanho + i)
    
    
   
    
