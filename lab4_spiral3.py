# This is my TA, Max Bond's code. It's super fun.
# I just added more circles, color, pensize variation and changed the angle.

import turtle

window = turtle.Screen()
myTurtle = turtle.Turtle()

myTurtle.speed(0)
turtle.bgcolor(1.0, 0.84, 0.0)

switcher = True #Makes it follow one rule every other time with if/else

for i in range(100):
    myTurtle.circle(i)

    if switcher:
        myTurtle.right(90)
        switcher = False
        myTurtle.color("yellow")
        myTurtle.pensize(2)

    else:
        myTurtle.right(30)
        switcher = True
        myTurtle.color("white")
        myTurtle.pensize(6)

    myTurtle.forward(5)

myTurtle.penup()
myTurtle.goto(200, 200)
myTurtle.pendown()

for i2 in range(100):
    myTurtle.circle(i2)

    if switcher:
        myTurtle.right(90)
        switcher = False
        myTurtle.color("purple")
        myTurtle.pensize(2)

    else:
        myTurtle.right(30)
        switcher = True
        myTurtle.color("blue")
        myTurtle.pensize(6)

    myTurtle.forward(5)

myTurtle.penup()
myTurtle.goto(-200, -200)
myTurtle.pendown()

for i3 in range(100):
    myTurtle.circle(i3)

    if switcher:
        myTurtle.right(90)
        switcher = False
        myTurtle.color("purple")
        myTurtle.pensize(2)

    else:
        myTurtle.right(30)
        switcher = True
        myTurtle.color("blue")
        myTurtle.pensize(6)

    myTurtle.forward(5)

myTurtle.penup()
myTurtle.goto(200, -200)
myTurtle.pendown()

for i4 in range(100):
    myTurtle.circle(i4)

    if switcher:
        myTurtle.right(90)
        switcher = False
        myTurtle.color(0.87, 0.72, 0.53)
        myTurtle.pensize(2)

    else:
        myTurtle.right(30)
        switcher = True
        myTurtle.color(0.80, 0.52, 0.25)
        myTurtle.pensize(6)

    myTurtle.forward(5)

myTurtle.penup()
myTurtle.goto(-200, 200)
myTurtle.pendown()

for i5 in range(100):
    myTurtle.circle(i5)

    if switcher:
        myTurtle.right(90)
        switcher = False
        myTurtle.color(0.87, 0.72, 0.53)
        myTurtle.pensize(2)

    else:
        myTurtle.right(30)
        switcher = True
        myTurtle.color(0.80, 0.52, 0.25)
        myTurtle.pensize(6)

    myTurtle.forward(5)

myTurtle.penup()
myTurtle.goto(400, 0)
myTurtle.pendown()

for i6 in range(100):
    myTurtle.circle(i6)

    if switcher:
        myTurtle.right(90)
        switcher = False
        myTurtle.color("yellow")
        myTurtle.pensize(2)

    else:
        myTurtle.right(30)
        switcher = True
        myTurtle.color("white")
        myTurtle.pensize(6)

    myTurtle.forward(5)

myTurtle.penup()
myTurtle.goto(-400, 0)
myTurtle.pendown()

for i7 in range(100):
    myTurtle.circle(i7)

    if switcher:
        myTurtle.right(90)
        switcher = False
        myTurtle.color("yellow")
        myTurtle.pensize(2)

    else:
        myTurtle.right(30)
        switcher = True
        myTurtle.color("white")
        myTurtle.pensize(6)

    myTurtle.forward(5)

turtle.hideturtle()

turtle.done()