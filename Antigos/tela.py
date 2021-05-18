import turtle
import random

def estaNaTela(tela,tar):
    if random.random() > 0.1:
        return True
    else:
        return False


peru = turtle.Turtle()
wn = turtle.Screen()

peru.shape('turtle')
while isInScreen(wn,peru):
    coin = random.randrange(0,2)
    if coin == 0:
        peru.left(90)
    else:
        peru.right(90)

    peru.forward(50)

wn.exitonclick()
