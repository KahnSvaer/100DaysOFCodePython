import random
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.colormode(1)


def square(turtle_pointer, length):
    for i in range(4):
        turtle_pointer.forward(length)
        turtle_pointer.right(90)


def dashed_list(turtle_pointer, length, repeat):
    for i in range(repeat):
        turtle_pointer.down()
        turtle_pointer.forward(length)
        turtle_pointer.up()
        turtle_pointer.forward(length)
        turtle_pointer.down()


def multiple_shapes(turtle_pointer, length, max_side):
    for total_sides in range(3, max_side + 1):
        angle = 360 / total_sides
        # noinspection PyTypeChecker
        turtle.pencolor(_random_color())
        for _ in range(total_sides):
            turtle_pointer.forward(length)
            turtle_pointer.right(angle)


def _random_color():
    color_channel = []
    for i in range(3):
        val = random.random()
        color_channel.append(val)
    return color_channel


def spirograph(turtle_pointer, radius, repeater):
    angle = 360/repeater
    for i in range(repeater):
        turtle_pointer.circle(radius)
        turtle_pointer.rt(angle)


def random_walk(turtle_pointer, length, repeat):
    angles = (0, 90, 180, 270)
    turtle_pointer.pensize(10)
    for _ in range(repeat):
        turtle_pointer.pencolor(_random_color())
        turtle_pointer.forward(length)
        new_angle = random.choice(angles)
        turtle_pointer.seth(new_angle)


spirograph(turtle, 25, 7)

screen.exitonclick()
