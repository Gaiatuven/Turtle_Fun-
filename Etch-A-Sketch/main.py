from turtle import Turtle, Screen


tk = Turtle()
screen = Screen()


def move_forwards():
    tk.forward(10)


def move_backwards():
    tk.backward(10)


def rotate_counter_clockwise():
    new_heading = tk.heading() + 10
    tk.setheading(new_heading)


def rotate_clockwise():
    new_heading = tk.heading() - 10
    tk.setheading(new_heading)


def clear_screen():
    tk.clear()
    tk.penup()
    tk.home()
    tk.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()

