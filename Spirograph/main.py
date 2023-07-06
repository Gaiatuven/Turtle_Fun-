import turtle as t
import random

greg = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        greg.forward(100)
        greg.right(angle)


for shape_side_n in range(3, 10):
    greg.color(random.choice(colours))
    draw_shape(shape_side_n)

# triangle = 120
# square = 90
# pentagon = 72
# hexagon = 60
# heptagon = 51.4
# octagon = 45
# nonage = 10
# decagon = 36
screen = Screen()
screen.exitonclick()
