import turtle

pen = turtle.Turtle()

def triangle():
    sides = 3
    while sides > 0:
        pen.forward(115.47)
        pen.left(120)
        sides = sides - 1
    pen.penup()
    pen.forward(135.53)
    pen.pendown()

def square():
    sides = 4
    while sides > 0:
        pen.forward(100)
        pen.left(90)
        sides = sides - 1
    pen.penup()
    pen.forward(120)
    pen.pendown()


square()
triangle()
turtle.done()

