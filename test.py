import turtle

pen = turtle.Pen() # this will give you reference to a pen
pen.speed(1)
colors = ["blue","purple","pink","turquoise"]

for x in range (100):
    c = colors[x%4]
    pen.pencolor(c)
    pen.forward(x+10)
    pen.right(90)