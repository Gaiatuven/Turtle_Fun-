import time
import turtle as turtle_module
import random

turtle_module.colormode(255)
tk = turtle_module.Turtle()
tk.speed("fastest")
tk.penup()
tk.hideturtle()

color_list = [(245, 245, 253), (250, 245, 251), (1, 1, 1), (2, 112, 240), (59, 180, 247), (250, 248, 243), (180, 54, 240), (1, 179, 247), (59, 101, 245), (242, 252, 247), (165, 4, 231), (13, 41, 225), (164, 174, 248), (201, 117, 239), (115, 218, 249), (218, 156, 244), (168, 24, 222), (0, 0, 4), (57, 37, 239), (164, 9, 250), (165, 161, 158), (98, 94, 91), (0, 4, 0), (7, 0, 5), (123, 235, 232), (13, 214, 213), (208, 97, 70), (206, 128, 33), (53, 222, 219), (227, 178, 162)]

tk.setheading(225)
tk.forward(300)
tk.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tk.dot(20, random.choice(color_list))
    tk.forward(50)

    if dot_count % 10 == 0:
        tk.setheading(90)
        tk.forward(50)
        tk.setheading(180)
        tk.forward(500)
        tk.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
turtle.done()