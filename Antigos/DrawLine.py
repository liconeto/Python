import turtle

def drawLsystem(aTurtle,instructions,angle,distance):
    savedInfoList = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            savedInfoList.append([aTurtle.heading(),aTurtle.xcor(),aTurtle.ycor()])
            print(savedInfoList)
        elif cmd == ']':
            newInfo = savedInfoList.pop()
            aTurtle.setheading(newInfo[0])
            aTurtle.setposition(newInfo[1],newInfo[2])
        else:
            print('Error:', cmd, 'is an unknown command')

t = turtle.Turtle()
inst = "FFFFFFFFFFFF[-FFFFFFFFFFFFFFFFFFFFFF[-FFFFFFFFFFFFFFF[-FFFFFBBBBB[-FFFFFFBBBBB[+FFFFFFBBBBB[+FFFFF"
t.setposition(0,-200)
t.left(90)
drawLsystem(t,inst,30,2)

