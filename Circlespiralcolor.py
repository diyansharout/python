import turtle
t = turtle.Pen()
t.speed(0)
# t.pencolor("blue")

for x in range(300):
    if x % 2 ==0:
        t.pencolor("blue")
    else:
        t.pencolor("pink")
    t.circle(x)
    t.left(30)


