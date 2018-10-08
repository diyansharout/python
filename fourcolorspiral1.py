import turtle
pen = turtle.Pen()
pen.speed(1)
colors = ["blue","purple","pink","turquoise"]
for x in range (1,6):
    pen.pencolor(colors[x % 4])
    pen.forward(50 * x)
    pen.right(218)

    # if x % 4 == 0:
    #     pen.pencolor("green")
    # elif x % 3 == 0:
    #     pen.pencolor("blue")
    # elif x % 2 == 0:
    #     pen.pencolor("pink")
    # else:
    #     pen.pencolor("purple")