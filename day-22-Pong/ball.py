import random
from math import copysign
from turtle import Turtle

BOUNDARY = (500, 280)
X_SPEED = (1, 3)
Y_SPEED = 4


class Ball:
    def __init__(self):
        self.turtle = Turtle()
        self.x_speed = self.random_speed()
        self.y_speed = Y_SPEED
        self.turtle.color("white")
        self.turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.turtle.shape("circle")
        self.turtle.speed("fastest")
        self.turtle.penup()

    def move(self):
        x_position = self.turtle.xcor()
        y_position = self.turtle.ycor()
        self.turtle.goto(x_position + self.x_speed, y_position + self.y_speed)

        # Collision with Walls
        if self.turtle.ycor() >= BOUNDARY[1]:
            self.y_speed *= -1
        elif self.turtle.ycor() <= -BOUNDARY[1]:
            self.y_speed *= -1

    def reset(self):
        self.turtle.home()
        self.y_speed = Y_SPEED
        self.random_speed()

    @staticmethod
    def random_speed():
        return random.randint(X_SPEED[0], X_SPEED[1])

    def x_position(self):
        return self.turtle.xcor()

    def bounce(self):
        self.x_speed = -copysign(self.random_speed(), self.x_speed)
