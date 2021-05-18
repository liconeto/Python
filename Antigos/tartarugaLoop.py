import turtle
import random

wn = turtle.Screen()
mole = turtle.Turtle()
mole.shape('turtle')
wn.bgcolor('lightgray')

def estaNaTela(tela, tar):
    if random.random() > 0.1:
        return True
    else:
        return False
	
while estaNaTela(wn, mole):
	coin = random.randrange(0,2)
	if coin == 0:
		mole.left(90)
	else:
		mole.right(90)
	mole.forward(50)
