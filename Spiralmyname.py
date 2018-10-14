import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "green", "purple"]
# Pop up window ( asking user for their name)
your_name = turtle.textinput ("Enter your name", "What is your name?")
for x in range(100):
    t.pencolor(colors[x % 4])
    t.penup()
    t.forward( x*4)
    t.pendown()
    t.write(your_name, font = ("Griffindor",int((x + 4)/4), "bold"))
    t.left(92)


