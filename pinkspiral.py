import turtle

window = turtle.Screen()
myTurtle = turtle.Turtle()
myTurtle.speed(0)

turtle.bgcolor(0.85, 0.43, 0.83) # Orchid

switcher = True #Makes it follow one rule every other time with if/else

# 1st Spiral

for i in range(300):
    myTurtle.circle(i, 180)

    if switcher:
        myTurtle.right(90)
        switcher = False
        myTurtle.color("white")
        myTurtle.pensize(5)

    else:
        myTurtle.right(45)
        switcher = True
        myTurtle.color("black")
        myTurtle.pensize(1)

    myTurtle.forward(5)

myTurtle.penup()
myTurtle.goto(15, -15)
myTurtle.pendown()

# 2nd Spiral

for i in range(150):
    myTurtle.circle(i, steps = 5)

    if switcher:
        myTurtle.right(90)
        switcher = False
        myTurtle.color(0.90, 0.93, 0.90) # Alice Blue
        myTurtle.pensize(5)

    else:
        myTurtle.right(30)
        switcher = True
        myTurtle.color("pink")
        myTurtle.pensize(5)

    myTurtle.forward(20)

myTurtle.penup()
myTurtle.goto(5, -20)
myTurtle.pendown()

# 3rd Spiral

for i in range(100):
    myTurtle.circle(i, steps = 5)

    if switcher:
        myTurtle.right(90)
        switcher = False
        myTurtle.color("dark grey")
        myTurtle.pensize(2)

    else:
        myTurtle.right(30)
        switcher = True
        myTurtle.color("grey")
        myTurtle.pensize(2)

    myTurtle.forward(20)

myTurtle.penup()
myTurtle.goto(0, 5)
myTurtle.pendown()

# 4th Spiral

for i in range(100):
    myTurtle.circle(i, steps = 3)

    if switcher:
        myTurtle.right(90)
        switcher = False
        myTurtle.color("white")
        myTurtle.pensize(2)

    else:
        myTurtle.right(45)
        switcher = True
        myTurtle.color(0.85, 0.43, 0.83) # Orchid)
        myTurtle.pensize(2)

    myTurtle.forward(5)

myTurtle.hideturtle()

turtle.done()