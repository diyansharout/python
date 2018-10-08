import turtle
t = turtle.Pen()
for x in range(60,100):
    if x % 2 == 0:
        t.speed(100)
        t.pencolor("red")
    else:
        t.speed(1)
    t.forward(x)
    t.left(90)


# for x in [10,11,12,13,14,15]:
#     print(x)

# for x in range(10,16):
#     print(x)

