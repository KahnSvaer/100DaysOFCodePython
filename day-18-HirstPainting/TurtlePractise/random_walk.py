from random import random, choice
from turtle import Turtle, Screen, colormode


def new_color():
    if colormode() != 1.0:
        colormode(1.0)  # With this we can directly use random.random()
    r = random()
    g = random()
    b = random()
    random_color = (r, g, b)
    return random_color


def new_angle():
    directions = [0, 90, 180, 270]
    return choice(directions)


def random_walk(marker, num_walk, forward_len, marker_width, marker_speed=5):
    marker.speed(marker_speed)
    marker.width(marker_width)
    for i in range(num_walk):
        marker.seth(new_angle())
        marker.color(new_color())
        marker.forward(forward_len)


turtle = Turtle()
random_walk(turtle, 500, 30, 15, 5)

screen = Screen()
screen.exitonclick()
