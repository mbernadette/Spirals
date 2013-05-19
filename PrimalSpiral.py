import turtle
turtle.speed(0)

for i in range(1, 36):
    for divisor in range(1, i):
        if i % divisor == 0:
            turtle.pensize(2)
            turtle.color("blue")
            turtle.right(45)
            turtle.forward(50)
        else:
            turtle.right(90)
            turtle.forward(100)
            break

turtle.hideturtle()
turtle.done()