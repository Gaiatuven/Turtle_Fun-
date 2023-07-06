import turtle
import turtle as t
import random

greg = t.Turtle()
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    colour = (r, g, b)
    return colour


directions = [0, 90, 180, 270]
greg.pensize(20)
greg.speed("fastest")

for _ in range(200):
    greg.color(random_colour())
    greg.forward(20)
    greg.setheading(random.choice(directions))

turtle.done()
