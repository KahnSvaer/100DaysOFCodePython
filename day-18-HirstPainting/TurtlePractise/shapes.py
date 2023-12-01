from turtle import Turtle, Screen
from random import random

def make_shape(marker, num_sides, side_len):
    angle = (360/num_sides)

    for _ in range(num_sides):
        marker.forward(side_len)
        marker.right(angle)


SIDE_LENGTH = 50


turtle = Turtle()
for i in range(4, 9):
    r = random()
    g = random()
    b = random()
    turtle.color(r, g, b)
    make_shape(turtle, i, SIDE_LENGTH)


screen = Screen()
screen.exitonclick()