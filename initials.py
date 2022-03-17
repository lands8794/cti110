import turtle

pen = turtle.Turtle()

turtle.Screen().bgcolor("black")
pen.color('white')
pen.pensize(20)

def initials():
    pen.penup()
    pen.left(90)
    pen.forward(25)
    pen.right(180)
    pen.pendown()
    pen.circle(25,235)
    pen.forward(35)
    pen.circle(-22,235)
    pen.penup()
    pen.right(180)
    pen.forward(20)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.pendown()
    pen.forward(104)
    pen.left(90)
    pen.forward(60)

initials()
turtle.done()