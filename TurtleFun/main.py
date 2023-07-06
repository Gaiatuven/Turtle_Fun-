import turtle

greg = turtle.Turtle()

greg.color("Blue","cyan")

for _ in range(4):
    greg.begin_fill()
    greg.forward(100)
    greg.left(90)
    greg.forward(100)
    greg.left(90)
    greg.forward(100)
    greg.left(90)
    greg.forward(100)

    greg.penup()
    greg.forward(20)
    greg.pendown()

    greg.end_fill()

# greg.forward(100)
# greg.left(90)
# greg.forward(100)
# greg.left(90)
# greg.forward(100)
# greg.left(90)
# greg.forward(100)
#
# greg.penup()
# greg.forward(20)
# greg.pendown()
#
# greg.forward(100)
# greg.left(90)
# greg.forward(100)
# greg.left(90)
# greg.forward(100)
# greg.left(90)
# greg.forward(100)
#
# greg.penup()
# greg.forward(20)
# greg.pendown()
#
# greg.forward(100)
# greg.left(90)
# greg.forward(100)
# greg.left(90)
# greg.forward(100)
# greg.left(90)
# greg.forward(100)



turtle.done()