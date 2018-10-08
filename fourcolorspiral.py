import turtle
pen = turtle.Pen()
pen.speed(100)
for x in range (1,200):
    pen.forward(2 * x)
    pen.right(91)

    if x % 4 == 0:
        pen.pencolor("green")
    elif x % 3 == 0:
        pen.pencolor("blue")
    elif x % 2 == 0:
        pen.pencolor("pink")
    else:
        pen.pencolor("purple")