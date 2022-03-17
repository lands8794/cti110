import turtle

pen = turtle.Turtle()

turtle.Screen().bgcolor("grey")
pen.color('white')
pen.pensize(3)

def twig():
    for i in range(3):
        pen.forward(60)
        pen.backward(60)
        pen.right(11.25)

def branch():
    for i in range(3):
        twig()
        pen.left(22.5)
        pen.backward(60)
        pen.left(11.25)
    pen.right(22.5)
    pen.forward(180)

def flake():
    pen.penup()
    pen.forward(180)
    pen.left(22.5)
    pen.pendown()
    for i in range(32):
        branch()
        pen.left(11.25)


flake()
turtle.done()