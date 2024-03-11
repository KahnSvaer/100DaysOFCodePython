import random
from turtle import Turtle


FINISH_LINE = 235


class Racer:
    def __init__(self, color, xcor, ycor):
        self.turtle = Turtle("turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(xcor, ycor)
        self.color = color

    def move(self):
        random_distance = random.random() * 10
        self.turtle.forward(random_distance)

    def is_finished(self):
        return self.turtle.xcor() > FINISH_LINE
