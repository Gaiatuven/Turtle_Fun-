import turtle
import turtle as t
import random

greg = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for _ in range(0, 10):
    greg.right(36)
    for _ in range(0, 5):
        greg.forward(100)
        greg.right(72)

turtle.done()