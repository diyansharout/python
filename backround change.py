import turtle
pen = turtle.Pen()
turtle.bgcolor("light blue")
pen.speed(1000)
colors = ["blue","purple","pink","turquoise"]
for x in range (1000):
    pen.pencolor(colors[x % 4])
    pen.forward(x)
    pen.right(91)